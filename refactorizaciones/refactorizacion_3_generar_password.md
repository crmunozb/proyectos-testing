
# Refactorización 3: Extracción de la lógica de generación de contraseñas

## 📌 Contexto
En main.py, cada vez que se crea un estudiante o supervisor se repite esta misma operación:

```python
password = generate_password_hash(matricula)
```
o
```python
password = generate_password_hash(password)
```

## 🎯 Motivo de elección
- Código repetido en múltiples lugares (crear estudiante, crear supervisor).
- Principio DRY (Don't Repeat Yourself) violado.
- Hace más difícil cambiar el esquema de generación de contraseñas en el futuro.

## 🧩 Problema detectado
Actualmente, si quisieras cambiar la forma de generar contraseñas, tendrías que buscar en muchos lugares del proyecto y actualizar manualmente cada línea.  
Esto aumenta el riesgo de errores y mantenimiento inconsistente.

## ✅ Solución propuesta: Crear una función utilitaria
Proponemos crear una función centralizada llamada generar_password:

```python
def generar_password(texto_base):
    """Genera un password seguro a partir de un texto base."""
    return generate_password_hash(texto_base)
```

## 🔨 Código refactorizado

**Antes (en varios lugares del código):**
```python
password = generate_password_hash(matricula)
# o
password = generate_password_hash(password)
```

**Después:**
```python
password = generar_password(matricula)
# o
password = generar_password(password)
```

**Definición de la función (idealmente en un archivo utils.py o al inicio de main.py):**
```python
def generar_password(texto_base):
    return generate_password_hash(texto_base)
```

## ✍️ Opinión y experiencia
Con esta refactorización:
- Se centralizó la responsabilidad de generación de contraseñas.
- El código quedó más limpio, reutilizable y mantenible.
- Si el método de hash cambia en el futuro, solo se cambia en un solo lugar.
