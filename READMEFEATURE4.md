# Feature 4 - Edición del Perfil de Usuario (Cristóbal)

Este módulo implementa **pruebas de aceptación automatizadas** usando el framework `Behave`, correspondientes a la Feature 4 del proyecto de testing.

El objetivo de esta funcionalidad es validar que un usuario pueda:

- Actualizar su nombre y correo electrónico.
- Cambiar su contraseña de forma segura.
- Recibir mensajes de error en caso de ingresar datos inválidos.

---

## 📁 Estructura del proyecto

```
CodeBending/
├── features/
│   ├── feature4.feature          # Escenarios escritos en Gherkin
│   └── steps/
│       └── steps_feature4.py     # Implementación de los pasos
├── requirements.txt              # Dependencias necesarias (incluye behave)
└── READMEFEATURE4.md             # Este documento
```

---

## 📦 Requisitos

- Python 3.6 o superior
- pip instalado
- Behave (`pip install behave`)

---

## 🛠️ Instalación de dependencias

Desde la carpeta del proyecto (`CodeBending`), ejecute:

```bash
pip install -r requirements.txt
```

---

## 🚀 Cómo ejecutar las pruebas

Ubicado en la carpeta `CodeBending`, corra el siguiente comando:

```bash
behave
```

El sistema ejecutará los escenarios definidos en `feature4.feature`.

---

## ✅ Escenarios cubiertos por esta Feature

1. ✅ **Actualización exitosa de nombre y correo electrónico**
2. ✅ **Cambio exitoso de contraseña**
3. ❌ **Error al intentar cambiar la contraseña con clave actual incorrecta**
4. ❌ **Error al intentar actualizar el correo con formato inválido**

Cada escenario está escrito siguiendo el lenguaje Gherkin (`Given`, `When`, `Then`) y validado con `assert` en los pasos Python.

---

## 🧪 Instrucciones para corrección (profesor)

Para probar esta Feature, siga los siguientes pasos desde la carpeta `CodeBending`:

1. **Instalar las dependencias necesarias** (solo una vez):

```bash
pip install -r requirements.txt
```

> Esto instalará `behave`, el framework que permite ejecutar las pruebas escritas en lenguaje natural.

2. **Ejecutar los escenarios de prueba:**

```bash
behave
```

3. **Interpretación del resultado:**

- Si todo está correcto, se mostrarán los 4 escenarios como `passed` en verde.
- Si alguna prueba falla, se indicará como `failed` con el motivo correspondiente.

No se requiere compilación adicional. Las pruebas se ejecutan directamente con Python.

---

## ✍️ Autor

**Cristóbal Muñoz Barrios**  
Estudiante de Ingeniería Civil Informática  
Universidad de Concepción  
Feature 4 – Pruebas de Aceptación: Edición del Perfil de Usuario  
Junio 2025
