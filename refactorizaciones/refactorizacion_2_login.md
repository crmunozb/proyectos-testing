
# Refactorización 2: Simplificación del método login() en main.py

## 📌 Contexto
El método login() se encarga de validar el inicio de sesión de estudiantes y supervisores. Se encuentra en la parte media del archivo main.py.

## 🎯 Motivo de elección
- El método tiene demasiada lógica embebida.
- Tiene duplicación de código al validar dos tipos de usuarios (Estudiante y Supervisor).
- Es difícil de testear por su dependencia de múltiples modelos y respuestas.

## 🧩 Problema detectado
- El método mezcla lógica de:
  - Captura de datos del formulario
  - Validación de dos tipos de usuario
  - Gestión de sesiones
  - Redirección con flash
- Esto viola el principio de responsabilidad única (SRP).
- Además, contiene duplicación:

```python
if estudiante and check_password_hash(...):
    ...
elif supervisor and check_password_hash(...):
    ...
```

## ✅ Solución propuesta: Aplicar Extract Method + Polymorphic Dispatch

Extraemos funciones auxiliares para separar responsabilidades:

| Nueva función | Responsabilidad |
|---------------|------------------|
| verificar_credenciales(correo, password) | Determina si hay un estudiante o supervisor válido |
| redirigir_usuario(usuario) | Redirige al dashboard correspondiente |
| gestionar_login(usuario) | Lógica común post-login |

## 🔨 Código refactorizado (boceto)

```python
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        correo = request.form['correo']
        password = request.form['password']

        usuario = verificar_credenciales(correo, password)
        if usuario:
            gestionar_login(usuario)
            return redirigir_usuario(usuario)
        flash('Credenciales inválidas', 'danger')

    return render_template('inicio.html')


def verificar_credenciales(correo, password):
    for modelo in [Estudiante, Supervisor]:
        usuario = modelo.query.filter_by(correo=correo).first()
        if usuario and check_password_hash(usuario.password, password):
            return usuario
    return None


def gestionar_login(usuario):
    login_user(usuario)
    flash('Has iniciado sesión exitosamente', 'success')


def redirigir_usuario(usuario):
    if isinstance(usuario, Estudiante):
        return redirect(url_for('dashEstudiante', estudiante_id=usuario.id))
    elif isinstance(usuario, Supervisor):
        return redirect(url_for('dashDocente', supervisor_id=usuario.id))
```

## ✍️ Opinión y experiencia
- El método login() ahora es compacto y claro.
- Eliminamos duplicación y lo hicimos extensible (si se agregara otro tipo de usuario).
- Facilita las pruebas unitarias y mejora el mantenimiento del código.
