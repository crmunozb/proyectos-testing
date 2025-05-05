
# Proyecto de Refactorización - CodeBending

Este repositorio corresponde al trabajo de refactorización realizado por el estudiante Cristóbal Muñoz Barrios sobre el proyecto **CodeBending**. El objetivo fue explorar el código fuente, identificar oportunidades de mejora y aplicar técnicas de refactorización para aumentar la legibilidad, mantenibilidad y calidad del software.

## 🎯 Objetivo

- Familiarizarse con el proyecto original.
- Detectar *code smells* o problemas de diseño presentes en el código.
- Aplicar al menos 3 refactorizaciones significativas.
- Documentar y justificar cada cambio realizado.

## 🛠️ Refactorizaciones realizadas

Se implementaron **4 refactorizaciones** en el proyecto, las cuales se encuentran documentadas en la carpeta `refactorizaciones/`.

A continuación, se presenta un resumen de cada una:

1. **Extract Method**
   - **Ubicación:** Clase `X`, método `Y`.
   - **Problema detectado:** Existencia de un método extenso y de difícil lectura.
   - **Solución aplicada:** Se extrajeron partes del código en métodos privados separados, mejorando la claridad y reduciendo la duplicación.

2. **Rename Variable**
   - **Ubicación:** Clase `A`, método `B`.
   - **Problema detectado:** Uso de nombres de variables poco descriptivos.
   - **Solución aplicada:** Se renombraron las variables para reflejar de mejor manera su propósito, facilitando la comprensión del código.

3. **Move Method**
   - **Ubicación:** Método `Z`.
   - **Problema detectado:** Presencia de un método ubicado en una clase que no correspondía a su lógica.
   - **Solución aplicada:** Se trasladó el método a la clase que realmente utilizaba sus datos, promoviendo la cohesión.

4. **Inline Temp**
   - **Ubicación:** Clase `C`.
   - **Problema detectado:** Uso innecesario de variables temporales.
   - **Solución aplicada:** Se reemplazaron las variables temporales por las expresiones directamente, simplificando el código.

## 📁 Estructura del repositorio

- `/refactorizaciones/`: Documentos y archivos que evidencian los cambios realizados, incluyendo comparaciones del código antes y después, y explicaciones detalladas.

---

# CodeBending

You need Java JRE > 21 installed and Apache Maven in your computer.

In your favorite virtual env :
`pip install -r requirements.txt`

Then to create the database :
`python .\crear_db.py`

Then to start the project :
`python .\main.py` 

Then you need to connect to http://127.0.0.1:3000/registerSupervisor to create the first supervsor account.

You can encounter an example of exercise for the platform here : https://github.com/GeoffreyHecht/FizzBuzzPasoAPaso

Important: There seems to be a problem with path management under Windows, so I recommend using Linux (or correcting the problem).
