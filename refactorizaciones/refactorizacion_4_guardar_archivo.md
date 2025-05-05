
# Refactorización 4: Extracción de la lógica de carga de archivos

## 📌 Contexto
En main.py, en funciones como agregarEjercicio o registrarEstudiantes, se repite manualmente el proceso de guardar archivos:

```python
archivo.save(os.path.join(ruta, archivo.filename))
```

Esta lógica está duplicada en varias partes del sistema.

## 🎯 Motivo de elección
- Código duplicado en varios controladores.
- Se repite lógica de:
  - Obtener ruta
  - Usar secure_filename
  - Guardar archivo en disco.
- No hay control unificado del nombre seguro del archivo (secure_filename).
- Difícil de mantener si cambia la lógica de guardado.

## 🧩 Problema detectado
- Código repetitivo.
- Riesgo de no usar secure_filename() consistentemente, lo que puede abrir vulnerabilidades de seguridad.

## ✅ Solución propuesta: Crear una función de utilidad para guardar archivos

Nueva función:

```python
from werkzeug.utils import secure_filename
import os

def guardar_archivo(archivo, ruta_destino):
    """Guarda un archivo de manera segura en la ruta destino."""
    nombre_archivo = secure_filename(archivo.filename)
    archivo.save(os.path.join(ruta_destino, nombre_archivo))
    return nombre_archivo
```

Así, en tus vistas ahora sólo escribes:

```python
nombre_archivo = guardar_archivo(archivo, app.config['UPLOAD_FOLDER'])
```

## 🔨 Código refactorizado

**Antes:**

```python
archivo = request.files['archivo']
archivo.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(archivo.filename)))
```

**Después:**

```python
archivo = request.files['archivo']
nombre_archivo = guardar_archivo(archivo, app.config['UPLOAD_FOLDER'])
```

## ✍️ Opinión y experiencia
Esta refactorización:
- Centralizó el manejo de archivos.
- Redujo la duplicación en múltiples funciones.
- Mejoró la seguridad de la aplicación.
- Facilitó el mantenimiento: si mañana cambias la política de nombres o la estructura de carpetas, sólo debes modificar una función.
