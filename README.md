# Trabajo Integrador Inteligencia Artificial y Sistemas Expertos

## Tema: Reconocimiento Facial con el lenguaje Python usando OpenCV y el método Local Binary Patterns Histograms (LBPH)

Profesoras: Alice Raquel Rambo y Graciela Sandra Zacharski

Autor: Jorge Fernando Rodriguez - LS00339

## Introducción

En este proyecto se realiza Reconocimiento Facial con el lenguaje Python usando OpenCV y el método Local Binary Patterns Histograms (LBPH).

### Python

Python es un lenguaje de programación popular y de alto nivel. Es conocido por su sintaxis clara y legible, lo que facilita escribir y entender código. Python es versátil y se utiliza en una variedad de campos, como desarrollo web, inteligencia artificial, análisis de datos y automatización de tareas.

Una de las fortalezas de Python es su comunidad activa y amplia biblioteca estándar, que proporciona una amplia gama de módulos y paquetes para facilitar el desarrollo de aplicaciones. Es un lenguaje interpretado, lo que significa que no requiere un paso adicional de compilación y es fácil de aprender para principiantes, pero también poderoso y flexible para proyectos más avanzados.

### OpenCV

OpenCV es un "kit de herramientas" para trabajar con imágenes y videos en una computadora. Ayuda a detectar objetos, seguir movimientos o reconocer caras en fotos y videos. Es muy popular porque es fácil de usar y tiene muchas funciones útiles.

### Local Binary Patterns Histograms (LBPH)

El método LBPH es una forma de enseñar a una computadora a reconocer caras en imágenes. En lugar de mirar los colores de la imagen, LBPH se enfoca en los patrones pequeños y detalles, como las texturas en la cara. Divide la cara en pedazos pequeños y comparas cómo se ven esos pedazos. Luego, se utiliza esta información para decirle a la computadora cómo es la cara de alguien. Es una forma efectiva de hacer que una computadora aprenda a reconocer rostros en fotos.

## Descripción de Carpetas y Archivos 

En un directorio, se crearon las siguientes carpetas:

* "datos" para almacenar los rostros de las personas que se desean reconocer.
* "videosPrueba" que contiene los videos con los cuales se probará el reconocimiento.

Del video llamado "Jorge-Entrenamiento.mp4" se obtienen los rostros para el entrenamiento. 

### Archivos

* capturaRostro.py: Script para capturar los rostros de las personas que se desea reconocer (lo que posteriormente será la base de datos). 
* entrenamientoLBPH.py: Entrenamiento del método Local Binary Patterns Histograms (LBPH). Luego del entrenamiento, se obtiene un modelo y se lo almacena.
* reconocimientoFacial.py: Lectura del modelo y prueba del reconocimiento facial. 

![Listado de Carpetas y Archivos](/capturasDePantalla/lista-carpetas-archivos.jpg)

## Pruebas

capturaRostro.py
![Captura Rostro](/capturasDePantalla/captura-rostro.jpg)

entrenamientoLBPH.py
![Captura Rostro](/capturasDePantalla/entrenamiento.jpg)

reconocimientoFacial.py
![Captura Rostro](/capturasDePantalla/reconocimiento-jorge.jpg)

![Captura Rostro](/capturasDePantalla/reconocimiento-desconocido.jpg)

## Bibliografía

Reconocimiento Facial | Python - OpenCV. Facebook. Youtube. Recuperado de: https://www.youtube.com/watch?v=cZkpaL36fW4 [03/01/2024].

OpenCV - Face Recognition with OpenCV. OpenCV. Recuperado de: https://docs.opencv.org/4.2.0/da/d60/tutorial_face_main.html [03/01/2024].

OpenCV - cv::face::LBPHFaceRecognizer Class Reference. Recuperado de: https://docs.opencv.org/3.4/df/d25/classcv_1_1face_1_1LBPHFaceRecognizer.html [04/01/2024].

Consultas sobre el código a ChatGPT. Recuperado de: https://openai.com/blog/chatgpt [05/01/2024].
















