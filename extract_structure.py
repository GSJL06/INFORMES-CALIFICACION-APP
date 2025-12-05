# Script temporal para extraer la estructura del PDF
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("No se encontró GEMINI_API_KEY en .env")

genai.configure(api_key=api_key)

# Subir el PDF
file_path = "Informe_formato_actual.pdf"
print(f"Subiendo archivo: {file_path}...")
uploaded_file = genai.upload_file(path=file_path, display_name="Informe Formato Actual")
print(f"Archivo subido. URI: {uploaded_file.uri}")

model = genai.GenerativeModel(model_name='models/gemini-2.5-flash')

prompt = """Analiza este informe PDF y extrae su estructura completa de forma muy detallada.

Por favor proporciona:

1. **ESTRUCTURA GENERAL DEL DOCUMENTO:**
   - Todas las secciones y subsecciones con sus títulos exactos
   - El orden de las páginas y contenido

2. **CAMPOS VARIABLES (que cambian por cliente):**
   - Lista todos los datos específicos del cliente que aparecen
   - Nombres, fechas, direcciones, códigos, etc.
   - Indica en qué sección aparece cada campo

3. **CONTENIDO FIJO (plantilla reutilizable):**
   - Textos que permanecen igual para todos los informes
   - Tablas con estructura fija
   - Procedimientos estándar

4. **TABLAS:**
   - Describe cada tabla encontrada
   - Columnas y estructura
   - Qué datos son variables vs fijos

5. **IMÁGENES/LOGOS:**
   - Qué imágenes aparecen
   - Dónde se ubican (encabezado, cuerpo, etc.)

6. **FORMATO:**
   - Estilo de encabezados
   - Numeración
   - Pies de página

Sé muy específico y detallado para poder recrear este formato en HTML."""

print("\nAnalizando estructura del PDF...")
response = model.generate_content([prompt, uploaded_file])

print("\n" + "="*80)
print("ESTRUCTURA DEL INFORME")
print("="*80)
print(response.text)

# Guardar resultado
with open("estructura_informe.md", "w", encoding="utf-8") as f:
    f.write("# Estructura del Informe - Formato Actual\n\n")
    f.write(response.text)
print("\n✅ Estructura guardada en: estructura_informe.md")

