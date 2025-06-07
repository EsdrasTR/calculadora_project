Calculadora de Raíces de Polinomios
Aplicación web desarrollada con Django y Python para calcular raíces de polinomios mediante métodos numéricos:
✅ Bisección
✅ Newton-Raphson
✅ Newton-Raphson Modificado

----Instalación-----
Requisitos previos
Python 3.8 o superior

pip (gestor de paquetes de Python)

Pasos para ejecutar el proyecto
Clonar el repositorio

bash

cd calculadora-raices
Crear y activar entorno virtual (Windows)

bash
python -m venv venv
venv\Scripts\activate
Instalar dependencias

bash
pip install -r requirements.txt
Ejecutar migraciones

bash
python manage.py migrate
Iniciar el servidor

bash
python manage.py runserver
Abrir en el navegador
 http://127.0.0.1:8000



----- Características---------
✔ Interfaz intuitiva con formularios dinámicos
✔ Gráficas interactivas usando Matplotlib
✔ Tabla de iteraciones para análisis detallado
✔ Validación de entrada para evitar errores
✔ Diseño responsive (funciona en móviles y PC)

------Uso------------
Ingresa la función polinómica (ej. x**3 - 2*x - 5)
Selecciona el método numérico
Proporciona los parámetros requeridos
Bisección: Intervalo [a, b], tolerancia, iteraciones
Newton-Raphson: Valor inicial x₀, tolerancia, iteraciones


Obtén resultados:
Raíz aproximada
Tabla de iteraciones
Gráfica de la función




------Tecnologías utilizadas--------
Backend: Python + Django
Frontend: HTML, CSS, Bootstrap
Métodos numéricos: NumPy, SymPy
Gráficas: Matplotlib



----------Estructura del proyecto-------------

calculadora-raices
├── calculadora_raices_project   # Configuración Django
├── metodos_numericos           # Lógica de la app
├── templates                   # Plantillas HTML
├── static                      # CSS/JS
├── manage.py
└── requirements.txt

-----Licencia----------------
MIT License - Libre uso y modificación.

-------Contacto--------------
¿Preguntas o sugerencias?
 eteleguarior@miumg.edu.gt

¡Calcula raíces de polinomios de forma eficiente!



