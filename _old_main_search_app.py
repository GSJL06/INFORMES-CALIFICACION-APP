# main.py

import os
import google.generativeai as genai
from dotenv import load_dotenv

# --- CONFIGURACIÓN INICIAL ---
# 1. Carga las variables del archivo .env (tu clave de API)
load_dotenv()

# 2. Configura el cliente de Gemini
try:
    genai.configure(api_key=os.environ["GEMINI_API_KEY"])
    print("Conexión exitosa a la API de Gemini.")
except Exception as e:
    print(f"Error al conectar con la API. ¿La clave está en .env? Detalle: {e}")
    exit()

# --- SUBIR ARCHIVO ---
# Sube tu archivo (Reemplaza 'Informe_de_calificacion_CES.pdf' con tu archivo real)
FILE_PATH = "Informe_de_calificacion_de_diseno.pdf"  # <-- ¡IMPORTANTE! Cambia esto

if not os.path.exists(FILE_PATH):
    print(f"\n¡ADVERTENCIA! No se encontró el archivo: {FILE_PATH}")
    print(f"Asegúrate de que el archivo '{FILE_PATH}' esté en la misma carpeta.")
    exit()

try:
    print(f"\nSubiendo archivo: {FILE_PATH}...")
    # Sube el archivo y obtén una referencia
    uploaded_file = genai.upload_file(path=FILE_PATH, display_name="Informe Anual de Calificación")
    print(f"Archivo subido exitosamente. URI: {uploaded_file.uri}")
except Exception as e:
    print(f"Error al subir el archivo: {e}")
    exit()

# --- CONSULTAR CON EL ARCHIVO ---



# 1. Define el modelo que usarás

# Usamos 'gemini-1.5-pro-latest' que es un modelo potente y multimodal.

model = genai.GenerativeModel(model_name="models/gemini-2.5-flash")



# 2. Pregunta y Obtén la Respuesta

# Esta es la pregunta que especificaste.

prompt = "Definir puntualmente que partes de ese informe se deben cambiar cuando se realice a otro cliente y cuales servirian para el informe de otro cliente"



print(f"\nGenerando respuesta para: '{prompt}'")

# El modelo analizará el archivo y la pregunta juntos

response = model.generate_content([prompt, uploaded_file])



print("\n--- Respuesta de Gemini (Fundamentada con tu archivo) ---")

print(response.text)



# La API para 'grounding_attributions' puede cambiar. Esta es una forma de verificarlo.

try:

    if response.prompt_feedback and response.prompt_feedback.grounding_attributions:

        print("\n--- Citas de la Fuente ---")

        for attribution in response.prompt_feedback.grounding_attributions:

            # La estructura de la atribución puede variar, esto es un ejemplo

            if hasattr(attribution, 'retrieved_content'):

                print(f"- Fragmento extraído de: {attribution.retrieved_content.file_name}")

            else:

                print("- Cita sin detalles de archivo.")

except Exception:

    # Si el método anterior falla, puede ser que la estructura sea otra.

    # No mostramos citas si no podemos encontrarlas para evitar errores.

    pass


