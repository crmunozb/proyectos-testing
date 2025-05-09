
# Refactorización 1: Extracción de métodos en main.py

## 📌 Contexto
El archivo main.py contiene funciones muy extensas, como procesar_archivo_csv, que gestiona tanto la creación de estudiantes, validaciones, como su inscripción a cursos.

## 🎯 Motivo de elección
- Long Method (Método Largo): procesar_archivo_csv supera las 90 líneas.
- Many Responsibilities: Hace múltiples tareas distintas (leer CSV, crear estudiante, inscribirlo, manejar errores, etc.).
- Difícil de testear y mantener.

## 🧩 Problema detectado
La función procesar_archivo_csv no respeta el Principio de Responsabilidad Única (SRP) ya que:
- Lee datos de un CSV.
- Valida el contenido de cada fila.
- Crea nuevos estudiantes si no existen.
- Inscribe estudiantes existentes a cursos.
- Gestiona errores de bases de datos.
- Muestra mensajes de error o éxito al usuario.

Esto la convierte en difícil de leer, propensa a errores y poco reutilizable.

## ✅ Solución propuesta: Aplicar Extract Method

Separar procesar_archivo_csv en funciones auxiliares:

| Nueva función propuesta | Responsabilidad principal |
|:---|:---|
| leer_archivo_csv(path) | Leer y parsear las filas del archivo CSV. |
| procesar_fila(row) | Validar y extraer los datos de cada fila. |
| crear_estudiante(matricula, apellidos, nombres, correo, carrera) | Crear un nuevo estudiante. |
| inscribir_estudiante(estudiante_id, curso_id) | Inscribir un estudiante en un curso. |

## 🔨 Código refactorizado (boceto inicial)

```python
def procesar_archivo_csv(filename, curso_id):
    filas = leer_archivo_csv(filename)
    for fila in filas:
        datos = procesar_fila(fila)
        if datos:
            matricula, apellidos, nombres, correo, carrera = datos
            estudiante = obtener_o_crear_estudiante(matricula, apellidos, nombres, correo, carrera)
            if estudiante:
                inscribir_estudiante(estudiante.id, curso_id)

def leer_archivo_csv(filename):
    with open(os.path.join(app.config['UPLOAD_FOLDER'], filename), 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Saltar cabecera
        return list(reader)

def procesar_fila(fila):
    if len(fila) != 5:
        current_app.logger.warning(f"La fila no tiene el formato esperado: {fila}")
        return None
    return fila

def obtener_o_crear_estudiante(matricula, apellidos, nombres, correo, carrera):
    estudiante = Estudiante.query.filter_by(matricula=matricula).first()
    if estudiante:
        return estudiante
    try:
        nuevo_estudiante = Estudiante(matricula=matricula, apellidos=apellidos, nombres=nombres, correo=correo, password=generate_password_hash(matricula), carrera=carrera)
        db.session.add(nuevo_estudiante)
        db.session.commit()
        return nuevo_estudiante
    except Exception as e:
        db.session.rollback()
        flash(f'Error al crear al registrar {nombres} {apellidos}.', 'warning')
        return None

def inscribir_estudiante(estudiante_id, curso_id):
    try:
        nueva_inscripcion = inscripciones.insert().values(id_estudiante=estudiante_id, id_curso=curso_id)
        db.session.execute(nueva_inscripcion)
        db.session.commit()
        flash(f'Estudiante inscrito en el curso.', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error al inscribir estudiante.', 'warning')
```

## ✍️ Opinión y experiencia grupal
Esta refactorización ayudó a:
- Clarificar responsabilidades de cada parte del proceso de carga de estudiantes.
- Facilitar pruebas unitarias individuales para cada función.
- Reducir el tamaño de procesar_archivo_csv en más de 70%.
- Mejorar el mantenimiento futuro ante cambios en el formato del CSV o en la validación de datos.

**Conclusión:** El código ahora esta mucho más ordenado, entendible y profesional
