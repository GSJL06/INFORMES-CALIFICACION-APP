# Estructura del Informe - Formato Actual

Este informe PDF presenta una estructura muy consistente y detallada, ideal para su recreación en HTML. A continuación, se desglosa su estructura completa:

---

### 1. ESTRUCTURA GENERAL DEL DOCUMENTO

El documento sigue una estructura modular con un encabezado y un pie de página fijos en cada página, y un contenido central que varía por sección.

**Orden de las páginas y contenido:**

*   **Página 1:**
    *   Encabezado del documento
    *   Proceso del documento
    *   **INFORMACIÓN PRINCIPAL**
        *   Campos de datos principales del informe.
    *   **OBJETIVO**
        *   Descripción del objetivo.
    *   **ALCANCE**
        *   Descripción del alcance.
    *   **RESPONSABILIDADES**
        *   Lista de responsabilidades.
    *   Pie de página de firma/aprobación.
*   **Página 2:**
    *   Encabezado del documento
    *   Proceso del documento
    *   Continuación de **RESPONSABILIDADES**
    *   **ELEMENTOS NECESARIOS**
        *   Materiales o suministros requeridos.
    *   **PROCEDIMIENTO**
        *   Lista numerada de pasos del procedimiento.
    *   **LISTA DE VERIFICACIÓN 1**
        *   Introducción a la tabla de verificación.
    *   Pie de página de firma/aprobación.
*   **Página 3-4:**
    *   Encabezado del documento
    *   Proceso del documento
    *   Tabla de **LISTA DE VERIFICACIÓN 1** (continuación en la P4).
    *   **Evidencias fotográficas de las actividades realizadas**
        *   Subsección: "1. Verificar la correcta transmisión..."
        *   Identificador de dispositivo.
    *   Pie de página de firma/aprobación.
*   **Página 5-9:**
    *   Encabezado del documento
    *   Proceso del documento
    *   Secciones visuales para cada dispositivo:
        *   Título del dispositivo (e.g., PRF196 NEVERA MED. FAST TRACK-P2-TA)
        *   Bloques de datos de Temperatura y Batería (con valor, fecha, hora).
    *   (Página 9) Subsección: "2. Segmentar el listado de variables..."
        *   Subsección: "Listado de dispositivos en prueba" (lista de dispositivos).
        *   Tabla de "Nombre responsable", "Teléfono", "Correo".
    *   Pie de página de firma/aprobación.
*   **Página 10-13:**
    *   Encabezado del documento
    *   Proceso del documento
    *   Subsección: "3. Verificar dentro del motor de alarmas..."
    *   Bloques de configuración de eventos para cada dispositivo:
        *   "Información del Evento" (Nombre de Variable, Organización, ID ubidots, Nombre del evento).
        *   "Configuración Límite Inferior".
        *   "Configuración Límite Superior".
        *   "Configuración de prioridad".
        *   "Contactos" (teléfonos, correos, fechas).
    *   Pie de página de firma/aprobación.
*   **Página 14-19:**
    *   Encabezado del documento
    *   Proceso del documento
    *   Subsección: "4. Ajustar los parámetros de configuración..."
    *   Subsección: "5. Registrar en la plantilla de control..."
    *   Bloques de resultados de prueba por dispositivo:
        *   Título del dispositivo.
        *   Detalles de la prueba (Inicio, Duración, Límites).
        *   Gráficos de temperatura con marca de excursión.
    *   Pie de página de firma/aprobación.
*   **Página 20-23:**
    *   Encabezado del documento
    *   Proceso del documento
    *   Subsección: "6. Ejecutar la prueba durante mínimo 5 minutos..."
    *   Subsección: "7. Restablecer los parámetros de configuración..."
    *   Subsección: "8. Verificar la transmisión y normalización..."
    *   Bloques de normalización de lecturas por dispositivo:
        *   Título del dispositivo.
        *   Gráficos de temperatura con marcas de duración de prueba y normalización.
    *   (Página 23) **LISTA DE VERIFICACIÓN 2**
        *   Subsección: "Cálculos y análisis estadísticos".
    *   Pie de página de firma/aprobación.
*   **Página 24:**
    *   Encabezado del documento
    *   Proceso del documento
    *   Texto introductorio a la tabla.
    *   Tabla de "LISTA DE VERIFICACIÓN 2" (tiempos de respuesta).
    *   **Evidencias fotográficas** (Título de sección, sin contenido visible en esta página).
    *   Pie de página de firma/aprobación.
*   **Página 25-28:**
    *   Encabezado del documento
    *   Proceso del documento
    *   Bloques de alertas por correo electrónico/SMS (representación visual de las notificaciones).
        *   Texto de la alerta (incluye dispositivo, registro, fecha, hora, URL).
        *   Botón "Presiona para cargar la vista previa".
    *   Pie de página de firma/aprobación.
*   **Página 29-30:**
    *   Encabezado del documento
    *   Proceso del documento
    *   **Evidencia fotográfica alertas correo electrónico** (Captura de pantalla de un buzón de Gmail).
    *   **LISTA DE VERIFICACIÓN 3**
        *   Subsección: "Criterios de aceptación v/s resultados de la prueba de desempeño".
        *   Tabla de criterios de aceptación.
    *   (Página 30) Continuación de la tabla de **LISTA DE VERIFICACIÓN 3**.
    *   Texto de referencia a evidencias fotográficas.
    *   **REFERENCIACIÓN NORMATIVA PARA EL PROCESO**
        *   Lista de normas.
    *   **INFORME DE DESVIACIONES**
        *   Descripción de desviaciones (si las hay), justificación, impacto.
    *   Pie de página de firma/aprobación.
*   **Página 31-32:**
    *   Encabezado del documento
    *   Proceso del documento
    *   Tabla de "Realizó desviación" y "Verificó desviación".
    *   **INFORME DE CALIFICACIÓN DE ESPECIFICACIONES FUNCIONALES**
        *   Subsección: "Resultados:" (Párrafo descriptivo).
        *   Subsección: "Conclusiones:" (Párrafo descriptivo, continuación en P32).
    *   (Página 32) Continuación de "Conclusiones:".
    *   Bloque de firmas (Realizó, Verificó, Aprobó).
    *   Pie de página de firma/aprobación.

---

### 2. CAMPOS VARIABLES (que cambian por cliente)

Estos son los datos que esperaríamos que cambien en cada informe o para cada cliente/configuración:

*   **Encabezado:**
    *   `Código:` `NXOP-IN-03`
    *   `Versión:` `01`
    *   `Vigencia:` `15/02/2025`
    *   `Página:` `X de Y` (X y Y son variables)
    *   `Proceso:` `Customer Success Manager`
*   **INFORMACIÓN PRINCIPAL (Página 1):**
    *   `Título:` `Sistema de telemetría Mi Monitor`
    *   `Nombre del establecimiento:` `Hospital Pablo Tobón Uribe`
    *   `Dirección del establecimiento:` `Calle 78 B # 69 - 240 N° 3`
    *   `Informe de calificación:` `N° 3`
    *   `Fecha calificación:` `09/07/2025`
*   **RESPONSABILIDADES (Página 1-2):**
    *   Los roles (`Personal de Netux`, `Tecnólogo Hospital`, `Ingeniero Netux`, `Ingeniero Hospital`) son fijos, pero las descripciones de las responsabilidades son variables en detalle si el alcance cambia.
*   **ELEMENTOS NECESARIOS (Página 2):**
    *   `micem@netuxtecnologia.com` (correo electrónico de contacto).
*   **LISTA DE VERIFICACIÓN 1 (Tabla, Página 3-4):**
    *   `Observación` (texto libre).
    *   `SI` / `NO` (marca 'X').
*   **Evidencias fotográficas... (Bloques de dispositivos, Página 4-9):**
    *   Nombres/IDs de dispositivos: `PRF196 NEVERA MED. FAST TRACK-P2-TA`, `PRF250 NEVERA MED. BODEGA FARM. E8-PB1-TB`, etc.
    *   Valores de `Temperatura` (e.g., `4.5°C`, `5.56°C`).
    *   Fechas y Horas de las lecturas (e.g., `16/07/2025 10:51 AM`).
    *   Valores de `Batería` (e.g., `4.1 Voltios`).
*   **Listado de dispositivos en prueba (Página 9):**
    *   La lista completa de IDs de dispositivos.
*   **Tabla de Contactos (Página 9):**
    *   `Nombre responsable`: `Yesid Hoyos`, `Darío Rojas`, `Luz Angela Angarita`, `Paola Arango`.
    *   `Teléfono`: `4459123`, `3502433321`, `3164433168`, etc.
    *   `Correo`: `yahoyos@hptu.org.co`, `laangarita@hptu.org.co`, `quimicoinvestigacion@hptu.org.co`.
*   **Configuración de eventos (Bloques, Página 10-13):**
    *   `Nombre de Variable`: `PRF196 NEVERA MED. FAST TRACK-P2-TA Temperatura`, etc.
    *   `Organización`: `HOSPITAL PABLO TOBÓN URIBE`.
    *   `ID ubidots`: `5e692e4c0ff4c3016d8eb8a9`, etc.
    *   `Nombre del evento`: `Desviación PRF196 NEVERA MED. FAST TRACK-P2-TA Temperatura`, etc.
    *   `Configuración Límite Inferior` -> `Valor limite inferior`: `2`.
    *   `Configuración Límite Superior` -> `Valor limite superior`: `8`.
    *   `Retardo` (en segundos o minutos): `1`.
    *   `Nivel de alarma`: `Alta`.
    *   `Intervalo de repeticiones (minutos)`: `20`.
    *   Fechas de "LOBO" (e.g., `2024-ago-16`, `2024-sep-1`).
    *   Números de teléfono y correos electrónicos en "Contactos" (los mismos de la tabla de P9, más `micem@netuxtecnologia.com`, `3178101080`, `3174374332`).
*   **Gráficos de prueba/normalización (Página 14-23):**
    *   `Inicio de prueba`: `10:06` (hora).
    *   `Duración`: `44 minutos`.
    *   `Límite superior`: `2°C`.
    *   `Límite inferior`: `8°C` o `7°C`.
    *   Valores de temperatura en los gráficos (ej. `44.44 °C`, `46.06 °C` en los puntos de excursión).
    *   Fechas y horas específicas dentro de los gráficos (ej. `09/07 10:06 AM`).
    *   Rango de fechas de los gráficos (`Fecha inicial: 09-jul. 0:00`, `Fecha final: 10-jul. 0:00`).
*   **LISTA DE VERIFICACIÓN 2 (Tabla, Página 24):**
    *   `Responsable`: `NETUX`.
    *   `Equipo`: Todos los IDs de dispositivos.
    *   `Envió correo electrónico?`: `SI`.
    *   `Envió mensaje de texto?`: `SI`.
    *   `Hora de inicio de la prueba`: `10:06`, `10:05`, `10:04`.
    *   `Hora de envió alerta`: `10:07`, `10:06`, `10:05`.
    *   `Retardo teórico`: `1`.
    *   `Retardo real`: `1` o `2`.
    *   `Cumplió retardo?`: `SI`.
*   **Evidencias fotográficas (Bloques de alertas, Página 25-28):**
    *   Texto de la alerta: `Alerta Netux - Desviacion de magnitudes, PRF196 NEVERA MED. FAST TRACK-P2-TA Temperatura registro 44.5 a las 2025-07-09 10:07:29 -0500 Inquietudes https://wa.link/j93foq.` (Todo este texto es variable, incluyendo nombre del dispositivo, valor, fecha, hora, URL).
*   **LISTA DE VERIFICACIÓN 3 (Tabla, Página 29-30):**
    *   Marca `X` en `Cumple` o `No Cumple`.
*   **INFORME DE DESVIACIONES (Página 30):**
    *   `Desviación (es):` `No se presentaron desviaciones`.
    *   `Justificación de la aceptación:` `No aplica`.
    *   `Impacto sobre la operación, función o proceso:` `No aplica`.
*   **Tabla de Realizó/Verificó desviación (Página 31):**
    *   `No aplica` (para Realizó/Verificó desviación).
    *   `Fecha: N/A`.
*   **INFORME DE CALIFICACIÓN DE ESPECIFICACIONES FUNCIONALES (Página 31-32):**
    *   Los párrafos de `Resultados` y `Conclusiones` son completamente variables, ya que describen los hallazgos específicos de la calificación. Contienen nombres de dispositivos (`AMBIENTE CUARTO CABLEADO E11-PB1-TB`, `CAVA #2 LACTEOS Y CARNES PB1-TB-SALAMANCA`, `ULTRACONGELADOR BANCO DE SANGRE E09-P3-TB`, etc.) y sus estados.
*   **Bloque de Firmas (Página 32, en el cuerpo):**
    *   `Maria Alejandra Zapata Chanci` (Nombre de quien realizó).
    *   `Rubén Darío Tabares Muñoz` (Nombre de quien verificó).
    *   `Daniel Antonio Quintero Rincón` (Nombre de quien aprobó).
    *   `Fecha:` `18/07/2025` (tres veces).
*   **Pie de página de firma/aprobación (Todas las páginas):**
    *   `Elaboró`: `Maria Alejandra Zapata Chanci`, `Customer Success Manager`, `NETUX SAS`.
    *   `Revisó`: `Ruben Darío Tabares`, `Director de operaciones`, `NETUX SAS`.
    *   `Aprobó`: `Daniel Antonio Quintero Rincón`, `Ingeniero Unidad de Mecánica y fluidos`, `Hospital Pablo Tobón Uribe`.
    *   `Fecha elaboración informe:` `18/07/2025`.

---

### 3. CONTENIDO FIJO (plantilla reutilizable)

Estos textos y estructuras son los mismos para todos los informes, salvo los campos variables mencionados:

*   **Logos y Título Principal:**
    *   Logo superior izquierdo ("EL HOSPITAL CON ALMA Pablo Tobón Uribe" y "netux").
    *   Título central: "INFORME DE CALIFICACION DE DESEMPEÑO SISTEMA DE TELEMETRÍA".
*   **Sección de Metadatos en Encabezado:**
    *   Las etiquetas "Código:", "Versión:", "Vigencia:", "Página:" son fijas.
*   **Proceso del Documento:**
    *   La etiqueta "Proceso:" es fija.
*   **Títulos de Secciones Principales (Nivel 1):**
    *   `INFORMACIÓN PRINCIPAL`
    *   `OBJETIVO`
    *   `ALCANCE`
    *   `RESPONSABILIDADES`
    *   `ELEMENTOS NECESARIOS`
    *   `PROCEDIMIENTO`
    *   `LISTA DE VERIFICACIÓN 1`
    *   `LISTA DE VERIFICACIÓN 2`
    *   `LISTA DE VERIFICACIÓN 3`
    *   `REFERENCIACIÓN NORMATIVA PARA EL PROCESO`
    *   `INFORME DE DESVIACIONES`
    *   `INFORME DE CALIFICACIÓN DE ESPECIFICACIONES FUNCIONALES`
*   **Subtítulos y Etiquetas Fijas:**
    *   `Título:`, `Nombre del establecimiento:`, `Dirección del establecimiento:`, `Informe de calificación:`, `Fecha calificación:` (en Información Principal).
    *   `Materiales o suministros necesarios para efectuar la calificación de desempeño` (en Elementos Necesarios).
    *   `Listado de usuario de Alarmas.`, `Orden de servicio con número de equipos a ejecutar la prueba`, `Computador con acceso a internet.`, `Acceso a correo electrónico` (en Elementos Necesarios - lista).
    *   `Ejecutar el procedimiento normal de las alarmas.`, `Adjuntar todos los formularios...`, `Completar el formulario resumen...`, etc. (en Procedimiento - lista numerada).
    *   `Registro de resumen de datos (a ser preparado para el procedimiento específico sometido a prueba)` (en Lista de Verificación 1 - párrafo).
    *   `Evidencias fotográficas de las actividades realizadas` (Título de Nivel 2).
    *   `1. Verificar la correcta transmisión y funcionalidad de las variables sometidas bajo prueba en la plataforma de monitoreo de telemetría.` (Título de Nivel 3).
    *   `Dispositivo` (etiqueta en bloques de datos de dispositivos).
    *   `Temperatura`, `Batería` (etiquetas en bloques de datos de dispositivos).
    *   Símbolos de temperatura (termómetro) y batería.
    *   `2. Segmentar el listado de variables bajo prueba y los contactos encargados de recibir las notificaciones (Vía mensaje SMS o Correo electrónico).` (Título de Nivel 3).
    *   `Listado de dispositivos en prueba` (Título de Nivel 4).
    *   `3. Verificar dentro del motor de alarmas de la plataforma los registros de configuración asociados a los requerimientos del cliente, tales como: Límites superior e inferior, Destinatarios de alarma (SMS y Correo electrónico).` (Título de Nivel 3).
    *   `A continuación, se presenta la configuración de los eventos asociados a los dispositivos que se utilizaron para hacer las pruebas.` (Página 10).
    *   `Información del Evento`, `Nombre de Variable`, `Organización`, `ID ubidots`, `Nombre del evento` (etiquetas en bloques de configuración de eventos).
    *   `Configuración Límite Inferior`, `Valor limite inferior(sin unidad)`, `Retardo` (etiquetas en bloques de configuración de eventos).
    *   `Configuración Límite Superior`, `Valor limite superior(sin unidad)`, `Retardo` (etiquetas en bloques de configuración de eventos).
    *   `Configuración de prioridad`, `Nivel de alarma`, `Intervalo de repeticiones (minutos)` (etiquetas en bloques de configuración de eventos).
    *   `Contactos`, `Llamada automática`, `+ Agregar Contactos` (etiquetas en bloques de configuración de eventos).
    *   `4. Ajustar los parámetros de configuración de las variables bajo prueba, para generar un "Ajuste virtual" que saque de especificaciones la lectura y genere una excursión que sobrepase los límites establecidos en las magnitudes medidas.` (Título de Nivel 3).
    *   `5. Registrar en la plantilla de control el primer dato en excursión luego de presentarse la excursión de temperatura del sensor.` (Título de Nivel 3).
    *   `Inicio de prueba:`, `Duración:`, `Límite superior:`, `Límite inferior:` (etiquetas en bloques de gráficos de prueba).
    *   `Fecha inicial:`, `Fecha final:`, `Q` (etiquetas en los gráficos).
    *   `6. Ejecutar la prueba durante mínimo 5 minutos, para la recepción de alarmas de los equipos sometidos a prueba.` (Título de Nivel 3).
    *   `7. Restablecer los parámetros de configuración de las variables bajo prueba, una vez hayan llegado las notificaciones de alarma de las mismas.` (Título de Nivel 3).
    *   `8. Verificar la transmisión y normalización de las lecturas de las variables bajo prueba, luego de restablecer a valores normales de funcionamiento` (Título de Nivel 3).
    *   `Tiempo de duración de la prueba`, `Normalización de temperatura` (etiquetas en los gráficos de normalización).
    *   `Cálculos y análisis estadísticos` (Título de Nivel 2 en Lista de Verificación 2).
    *   `Una vez realizada la prueba de alarma del sistema de telemetría, se registra en la lista de verificación 2 los tiempos de respuesta obtenidos durante la ejecución de la prueba del sistema, así como la evidencia de la recepción de las notificaciones a los usuarios finales (Se adjunta a este informe las pruebas a todas las variables).` (Página 24, texto introductorio a la tabla).
    *   `Evidencia fotográfica alertas correo electrónico` (Título de Nivel 2).
    *   `Presiona para cargar la vista previa` (en bloques de alertas).
    *   `Criterios de aceptación v/s resultados de la prueba de desempeño` (Título de Nivel 2 en Lista de Verificación 3).
    *   `Las evidencias fotográficas de los criterios de aceptación mostrados en la lista de verificación 3, se pueden ver a detalle en el informe 'Informe de calificación de diseño del sistema de telemetría'` (Página 30, texto de referencia).
    *   `GAMP 5: Risk-Based Approach to Compliant GxP Computerized Systems, International Society for Pharmaceutical Engineering(ISPE), 2008, United states.` (Referencia normativa).
    *   `Colombia. Ministerio de la Protección Social. (2009). N° 6, Articulo 6 RESOLUCIÓN 4410 DE 2009` (Referencia normativa).
    *   `Desviación (es):`, `Justificación de la aceptación:`, `Impacto sobre la operación, función o proceso:` (etiquetas en Informe de Desviaciones).
    *   `Realizó desviación`, `Verificó desviación`, `Fecha:` (etiquetas en la tabla de desviaciones).
    *   `Resultados:`, `Conclusiones:` (subtítulos en Informe de Calificación de Especificaciones Funcionales).
    *   `Realizó`, `Verificó`, `Aprobó` (etiquetas en el bloque de firmas final).

*   **Pie de página de firma/aprobación (Tabla):**
    *   Estructura de la tabla de 3x3 celdas con etiquetas `Elaboró`, `Revisó`, `Aprobó` y los títulos de cargo (`Customer Success Manager`, `Director de operaciones`, `Ingeniero Unidad de Mecánica y fluidos`).
    *   Línea `Fecha elaboración informe:`.

---

### 4. TABLAS

Se identifican varias tablas:

1.  **Tabla 1: LISTA DE VERIFICACIÓN 1 (Página 3-4)**
    *   **Estructura:** Tabla con 4 columnas principales.
    *   **Columnas:**
        *   `Ítem Número`: Fijo (números 1 al 8).
        *   `Actividad`: Fijo (descripciones de pasos).
        *   `Observación`: Variable (texto libre, aquí aparece "Sin novedad").
        *   `Ítem Cumplido`: Dividida en dos subcolumnas:
            *   `SI`: Variable (marca 'X').
            *   `NO`: Variable (marca 'X').
    *   **Datos Variables vs Fijos:** Las actividades y la numeración son fijas. Las "Observaciones" y las marcas "X" en "SI" o "NO" son variables.

2.  **Tabla 2: Contactos (Página 9)**
    *   **Estructura:** Tabla con 3 columnas.
    *   **Columnas:**
        *   `Nombre responsable`: Variable (nombre de persona o departamento).
        *   `Teléfono`: Variable (número de teléfono).
        *   `Correo`: Variable (dirección de correo electrónico).
    *   **Datos Variables vs Fijos:** Los encabezados de las columnas son fijos. Todo el contenido de las filas es variable.

3.  **Tabla 3: Información de Eventos (Página 10-13, formato de tabla/formulario)**
    *   **Estructura:** Cada dispositivo tiene un bloque que actúa como una tabla/formulario, agrupando información.
    *   **Columnas/Campos (dentro de cada bloque):**
        *   `Nombre de Variable`: Variable.
        *   `Organización`: Variable (siempre `HOSPITAL PABLO TOBÓN URIBE` en este ejemplo, pero podría ser variable).
        *   `ID ubidots`: Variable (código alfanumérico).
        *   `Nombre del evento`: Variable.
        *   `Configuración Límite Inferior` (Sección):
            *   `Valor limite inferior(sin unidad)`: Variable (valor numérico).
            *   `Retardo`: Variable (valor numérico).
        *   `Configuración Límite Superior` (Sección):
            *   `Valor limite superior(sin unidad)`: Variable (valor numérico).
            *   `Retardo`: Variable (valor numérico).
        *   `Configuración de prioridad` (Sección):
            *   `Nivel de alarma`: Variable (`Alta`).
            *   `Intervalo de repeticiones (minutos)`: Variable (valor numérico).
        *   `Contactos` (Sección): Contiene números de teléfono y direcciones de correo electrónico, todos variables.
        *   Fechas de "LOBO": Dos fechas (e.g., `2024-ago-16`, `2024-sep-1`), variables.
    *   **Datos Variables vs Fijos:** Las etiquetas (e.g., "Nombre de Variable", "Valor limite inferior", "Retardo") y la estructura general de los bloques son fijas. Todos los valores asociados a estas etiquetas son variables.

4.  **Tabla 4: LISTA DE VERIFICACIÓN 2 (Página 24)**
    *   **Estructura:** Tabla con 9 columnas.
    *   **Columnas:**
        *   `Responsable`: Variable (`NETUX`).
        *   `Equipo`: Variable (IDs de dispositivos).
        *   `Envió correo electrónico?`: Variable (`SI`).
        *   `Envió mensaje de texto?`: Variable (`SI`).
        *   `Hora de inicio de la prueba`: Variable (hora).
        *   `Hora de envió alerta`: Variable (hora).
        *   `Retardo teórico`: Variable (valor numérico).
        *   `Retardo real`: Variable (valor numérico).
        *   `Cumplió retardo?`: Variable (`SI`).
    *   **Datos Variables vs Fijos:** Los encabezados de las columnas son fijos. Todo el contenido de las filas es variable.

5.  **Tabla 5: LISTA DE VERIFICACIÓN 3 (Página 29-30)**
    *   **Estructura:** Tabla con 3 columnas.
    *   **Columnas:**
        *   `Criterios de aceptación`: Fijo (descripciones de los criterios).
        *   `Cumple`: Variable (marca 'X').
        *   `No Cumple`: Variable (marca 'X').
    *   **Datos Variables vs Fijos:** Los encabezados de las columnas y los textos de los criterios son fijos. Las marcas 'X' son variables.

6.  **Tabla 6: Realizó/Verificó Desviación (Página 31)**
    *   **Estructura:** Tabla simple de 2 filas y 2 columnas para el cuerpo, más una fila de encabezado.
    *   **Columnas:**
        *   (Sin encabezado específico para la primera columna, es implícitamente el rol)
        *   `Realizó desviación`: Fijo, texto libre debajo.
        *   `Fecha:`: Fijo.
        *   `Verificó desviación`: Fijo, texto libre debajo.
        *   `Fecha:`: Fijo.
    *   **Datos Variables vs Fijos:** La estructura de la tabla y las etiquetas (`Realizó desviación`, `Fecha:`, `Verificó desviación`) son fijas. Los valores como `No aplica` y `N/A` son variables (aunque en este informe aparecen como "No aplica" fijo).

7.  **Tabla 7: Pie de Página de Firmas (Inferior de cada página)**
    *   **Estructura:** Tabla de 3x3 celdas, con encabezados de columna implícitos.
    *   **Columnas:** `Elaboró`, `Revisó`, `Aprobó`.
    *   **Contenido de filas:**
        *   Fila 1: Nombre de la persona (Variable).
        *   Fila 2: Cargo (Fijo).
        *   Fila 3: Empresa/Departamento (Fijo).
    *   **Datos Variables vs Fijos:** Los encabezados de las columnas (`Elaboró`, `Revisó`, `Aprobó`), los cargos y las empresas/departamentos son fijos. Los nombres de las personas son variables. La línea "Fecha elaboración informe: [Fecha Variable]" es también parte de este pie de página.

---

### 5. IMÁGENES/LOGOS

*   **Logo "EL HOSPITAL CON ALMA Pablo Tobón Uribe"**: Ubicado en el encabezado izquierdo de cada página. Es un logo combinado con texto.
*   **Logo "netux"**: Ubicado debajo del logo del hospital en el encabezado izquierdo de cada página.
*   **Icono de Termómetro**: Aparece junto a las lecturas de "Temperatura" en los bloques de datos de dispositivos (Página 5-9).
*   **Icono de Batería**: Aparece junto a las lecturas de "Batería" en los bloques de datos de dispositivos (Página 5-9).
*   **Captura de pantalla de correo electrónico (Gmail)**: Ubicado en el cuerpo de la Página 29, mostrando una lista de alertas de telemetría. Este es un bloque de imagen que contiene texto que a su vez tiene una estructura repetitiva.
*   **Firmas manuscritas**: Ubicadas en el bloque de firmas final en la Página 32, sobre los nombres de las personas. Estas son imágenes de firmas.
*   **Gráficos de Temperatura**: Todas las páginas con gráficos (14-23) contienen imágenes o representaciones visuales de los datos de temperatura, con ejes, líneas y puntos de datos. Son generados dinámicamente, por lo que su contenido visual es variable, aunque su estilo y etiquetas de ejes son fijos.

---

### 6. FORMATO

*   **Estilo de encabezados:**
    *   **Nivel 1 (Secciones Principales):** Texto en mayúsculas, negrita, tamaño de fuente grande (ej. `INFORMACIÓN PRINCIPAL`).
    *   **Nivel 2 (Subsecciones):** Texto en negrita, tamaño de fuente mediano (ej. `Evidencias fotográficas de las actividades realizadas`).
    *   **Nivel 3 (Sub-subsecciones/Items de procedimiento/dispositivos):** Texto en negrita, a menudo numerado (ej. `1. Verificar la correcta transmisión y funcionalidad...`, `PRF196 NEVERA MED. FAST TRACK-P2-TA`).
    *   **Nivel 4:** Texto en negrita, más pequeño (ej. `Listado de dispositivos en prueba`).
*   **Numeración:**
    *   Listas de responsabilidades y elementos necesarios: Viñetas (`•`).
    *   Procedimiento: Numérica (`1.`, `2.`, `3.`).
    *   Subsecciones de "Evidencias fotográficas": Numérica (`1.`, `2.`, `3.`).
    *   Paginación: Numérica (`X de Y`).
*   **Pies de página:**
    *   Consistente en todas las páginas.
    *   Contiene una tabla con tres columnas: `Elaboró`, `Revisó`, `Aprobó`.
    *   Cada columna tiene el nombre de la persona, su cargo y la empresa/departamento.
    *   Debajo de esta tabla, se encuentra la línea `Fecha elaboración informe: [Fecha]`.
    *   El texto dentro de la tabla del pie de página está alineado a la izquierda dentro de cada celda.
*   **General:**
    *   **Fuentes:** Aparentemente una fuente sans-serif consistente a lo largo del documento (tipo Arial o Helvetica).
    *   **Alineación:** La mayoría del texto del cuerpo está alineado a la izquierda.
    *   **Espaciado:** Espaciado consistente entre párrafos y elementos de lista.
    *   **Bloques de Información:** Muchos datos se presentan en bloques visualmente delimitados (ej. datos de temperatura/batería, configuraciones de eventos, alertas), a menudo con un borde implícito o un fondo ligeramente distinto (aunque no se ve en el OCR en blanco y negro, es una buena práctica considerar en HTML).
    *   **Gráficos:** Usan ejes claros, etiquetas de unidades (`°C`, `Voltios`), y marcas de tiempo/fecha.
    *   **Uso de Negrita:** Se utiliza extensivamente para títulos, subtítulos y elementos clave para enfatizar.