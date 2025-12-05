# app.py
# Aplicación Flask para generación de Informes de Calificación de Desempeño

import os
import uuid
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash, send_file, session
from werkzeug.utils import secure_filename
import base64

# Configuración de la aplicación
app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')

# Ruta base del proyecto
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_FOLDER = os.path.join(BASE_DIR, 'static')

# Configuración de uploads
UPLOAD_FOLDER = os.path.join(STATIC_FOLDER, 'uploads')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH
app.config['STATIC_FOLDER'] = STATIC_FOLDER

# Crear carpetas necesarias
os.makedirs(os.path.join(UPLOAD_FOLDER, 'logos'), exist_ok=True)
os.makedirs(os.path.join(UPLOAD_FOLDER, 'evidencias'), exist_ok=True)
os.makedirs(os.path.join(UPLOAD_FOLDER, 'firmas'), exist_ok=True)
os.makedirs(os.path.join(UPLOAD_FOLDER, 'graficos'), exist_ok=True)


def get_image_base64(filepath):
    """Convertir imagen a base64 para incrustar en HTML/PDF"""
    try:
        full_path = os.path.join(STATIC_FOLDER, filepath) if not os.path.isabs(filepath) else filepath
        if os.path.exists(full_path):
            with open(full_path, 'rb') as f:
                data = f.read()
            ext = filepath.rsplit('.', 1)[-1].lower()
            mime_type = {'png': 'image/png', 'jpg': 'image/jpeg', 'jpeg': 'image/jpeg', 'gif': 'image/gif'}.get(ext, 'image/png')
            return f"data:{mime_type};base64,{base64.b64encode(data).decode('utf-8')}"
    except Exception as e:
        print(f"Error cargando imagen {filepath}: {e}")
    return None


def allowed_file(filename):
    """Verificar si el archivo tiene una extensión permitida"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def generate_unique_filename(filename):
    """Generar nombre único para archivos subidos"""
    ext = filename.rsplit('.', 1)[1].lower() if '.' in filename else ''
    unique_name = f"{uuid.uuid4().hex}.{ext}"
    return unique_name


# ============== RUTAS PRINCIPALES ==============

@app.route('/')
def index():
    """Página principal - Formulario de entrada de datos"""
    return render_template('index.html')


@app.route('/generar', methods=['POST'])
def generar_informe():
    """Procesar formulario y generar informe"""
    try:
        # Recopilar datos del formulario
        datos = {
            # Metadatos del documento
            'codigo': request.form.get('codigo', 'NXOP-IN-03'),
            'version': request.form.get('version', '01'),
            'vigencia': request.form.get('vigencia', ''),
            'proceso': request.form.get('proceso', 'Customer Success Manager'),

            # Información principal
            'titulo': request.form.get('titulo', 'Sistema de telemetría Mi Monitor'),
            'nombre_establecimiento': request.form.get('nombre_establecimiento', ''),
            'direccion_establecimiento': request.form.get('direccion_establecimiento', ''),
            'numero_informe': request.form.get('numero_informe', ''),
            'fecha_calificacion': request.form.get('fecha_calificacion', ''),

            # Responsables Netux
            'elaboro_nombre': request.form.get('elaboro_nombre', ''),
            'elaboro_cargo': request.form.get('elaboro_cargo', 'Customer Success Manager'),
            'reviso_nombre': request.form.get('reviso_nombre', ''),
            'reviso_cargo': request.form.get('reviso_cargo', 'Director de operaciones'),

            # Responsables Cliente
            'aprobo_nombre': request.form.get('aprobo_nombre', ''),
            'aprobo_cargo': request.form.get('aprobo_cargo', ''),
            'aprobo_entidad': request.form.get('aprobo_entidad', ''),

            # Fecha elaboración
            'fecha_elaboracion': request.form.get('fecha_elaboracion', ''),

            # Resultados y conclusiones
            'resultados': request.form.get('resultados', ''),
            'conclusiones': request.form.get('conclusiones', ''),

            # Desviaciones
            'desviaciones': request.form.get('desviaciones', 'No se presentaron desviaciones'),
            'justificacion_desviacion': request.form.get('justificacion_desviacion', 'No aplica'),
            'impacto_desviacion': request.form.get('impacto_desviacion', 'No aplica'),
        }

        # Procesar dispositivos (múltiples) con evidencias
        dispositivos = []
        dispositivo_nombres = request.form.getlist('dispositivo_nombre[]')
        dispositivo_evidencias = request.files.getlist('dispositivo_evidencia[]')

        for i in range(len(dispositivo_nombres)):
            if dispositivo_nombres[i]:
                dispositivo = {
                    'nombre': dispositivo_nombres[i],
                    'evidencia': None
                }
                # Procesar evidencia del dispositivo
                if i < len(dispositivo_evidencias):
                    file = dispositivo_evidencias[i]
                    if file and file.filename and allowed_file(file.filename):
                        filename = generate_unique_filename(file.filename)
                        filepath = os.path.join(app.config['UPLOAD_FOLDER'], 'evidencias', filename)
                        file.save(filepath)
                        dispositivo['evidencia'] = f'uploads/evidencias/{filename}'
                dispositivos.append(dispositivo)
        datos['dispositivos'] = dispositivos

        # Procesar contactos
        contactos = []
        contacto_nombres = request.form.getlist('contacto_nombre[]')
        contacto_telefonos = request.form.getlist('contacto_telefono[]')
        contacto_correos = request.form.getlist('contacto_correo[]')

        for i in range(len(contacto_nombres)):
            if contacto_nombres[i]:
                contactos.append({
                    'nombre': contacto_nombres[i],
                    'telefono': contacto_telefonos[i] if i < len(contacto_telefonos) else '',
                    'correo': contacto_correos[i] if i < len(contacto_correos) else '',
                })
        datos['contactos'] = contactos

        # Manejar uploads de imágenes
        # Logo del cliente
        if 'logo_cliente' in request.files:
            file = request.files['logo_cliente']
            if file and file.filename and allowed_file(file.filename):
                filename = generate_unique_filename(file.filename)
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], 'logos', filename)
                file.save(filepath)
                datos['logo_cliente'] = f'uploads/logos/{filename}'

        # Evidencias fotográficas
        evidencias = []
        if 'evidencias[]' in request.files:
            files = request.files.getlist('evidencias[]')
            for file in files:
                if file and file.filename and allowed_file(file.filename):
                    filename = generate_unique_filename(file.filename)
                    filepath = os.path.join(app.config['UPLOAD_FOLDER'], 'evidencias', filename)
                    file.save(filepath)
                    evidencias.append(f'uploads/evidencias/{filename}')
        datos['evidencias'] = evidencias

        # Guardar datos en sesión para vista previa
        session['datos_informe'] = datos

        return redirect(url_for('preview'))

    except Exception as e:
        flash(f'Error al procesar el formulario: {str(e)}', 'error')
        return redirect(url_for('index'))


@app.route('/preview')
def preview():
    """Vista previa del informe generado"""
    datos = session.get('datos_informe')
    if not datos:
        flash('No hay datos de informe para mostrar', 'warning')
        return redirect(url_for('index'))

    return render_template('informe_desempeno.html', datos=datos, preview_mode=True)


@app.route('/descargar/<formato>')
def descargar(formato):
    """Descargar informe en formato especificado"""
    datos = session.get('datos_informe')
    if not datos:
        flash('No hay datos de informe para descargar', 'warning')
        return redirect(url_for('index'))

    # Preparar datos con imágenes en base64 para PDF
    datos_pdf = datos.copy()

    # Convertir logo de Netux a base64
    netux_logo_path = os.path.join(STATIC_FOLDER, 'Netux_Logo.png')
    datos_pdf['netux_logo_base64'] = get_image_base64(netux_logo_path)

    # Convertir logo del cliente a base64 si existe
    if datos.get('logo_cliente'):
        datos_pdf['logo_cliente_base64'] = get_image_base64(datos['logo_cliente'])

    # Convertir evidencias de dispositivos a base64
    if datos.get('dispositivos'):
        dispositivos_pdf = []
        for disp in datos['dispositivos']:
            disp_pdf = disp.copy()
            if disp.get('evidencia'):
                disp_pdf['evidencia_base64'] = get_image_base64(disp['evidencia'])
            dispositivos_pdf.append(disp_pdf)
        datos_pdf['dispositivos'] = dispositivos_pdf

    # Convertir evidencias generales a base64
    if datos.get('evidencias'):
        evidencias_base64 = []
        for ev in datos['evidencias']:
            ev_b64 = get_image_base64(ev)
            if ev_b64:
                evidencias_base64.append(ev_b64)
        datos_pdf['evidencias_base64'] = evidencias_base64

    if formato == 'html':
        # Generar HTML con imágenes base64 para que funcionen offline
        html_content = render_template('informe_desempeno.html', datos=datos_pdf, preview_mode=False, pdf_mode=True)

        # Guardar temporalmente
        temp_path = os.path.join(app.config['UPLOAD_FOLDER'], 'temp_informe.html')
        with open(temp_path, 'w', encoding='utf-8') as f:
            f.write(html_content)

        return send_file(
            temp_path,
            as_attachment=True,
            download_name=f"Informe_Calificacion_Desempeno_{datos.get('nombre_establecimiento', 'cliente')}.html"
        )

    elif formato == 'pdf':
        try:
            from weasyprint import HTML

            html_content = render_template('informe_desempeno.html', datos=datos_pdf, preview_mode=False, pdf_mode=True)

            # Generar PDF con base_url apuntando a la carpeta static
            temp_pdf = os.path.join(app.config['UPLOAD_FOLDER'], 'temp_informe.pdf')
            HTML(string=html_content, base_url=STATIC_FOLDER).write_pdf(temp_pdf)

            return send_file(
                temp_pdf,
                as_attachment=True,
                download_name=f"Informe_Calificacion_Desempeno_{datos.get('nombre_establecimiento', 'cliente')}.pdf"
            )
        except ImportError:
            flash('WeasyPrint no está instalado. Use: pip install weasyprint', 'error')
            return redirect(url_for('preview'))

    flash('Formato no soportado', 'error')
    return redirect(url_for('preview'))


@app.route('/limpiar')
def limpiar():
    """Limpiar datos de sesión y empezar nuevo informe"""
    session.pop('datos_informe', None)
    flash('Datos limpiados. Puede iniciar un nuevo informe.', 'success')
    return redirect(url_for('index'))


# ============== CONTEXTO GLOBAL ==============

@app.context_processor
def utility_processor():
    """Variables y funciones disponibles en todas las plantillas"""
    return {
        'now': datetime.now(),
        'app_name': 'Generador de Informes de Calificación',
        'company': 'NETUX SAS'
    }


# ============== EJECUCIÓN ==============

if __name__ == '__main__':
    print("=" * 60)
    print("  GENERADOR DE INFORMES DE CALIFICACIÓN DE DESEMPEÑO")
    print("  NETUX SAS - Sistema de Telemetría")
    print("=" * 60)
    print(f"\n  Servidor corriendo en: http://127.0.0.1:5000")
    print("  Presiona Ctrl+C para detener\n")
    app.run(debug=True, host='0.0.0.0', port=5000)
