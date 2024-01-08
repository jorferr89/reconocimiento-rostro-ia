# Reconocimiento Facial con el lenguaje Python usando OpenCV y el método Local Binary Patterns Histograms (LBPH) 

### Materia: Inteligencia Artificial y Sistemas Expertos

### Año: 2024

### Profesoras: Alice Raquel Rambo y Graciela Sandra Zacharski

### Autor: Jorge Fernando Rodriguez - LS00339

## Introducción

En este proyecto se realiza Reconocimiento Facial con el lenguaje Python usando OpenCV y el método Local Binary Patterns Histograms (LBPH).

En primer lugar se recolectarán los datos (los rostros de las personas que se desee reconocer), luego entrenaremos el clasificador, para finalmente realizar las pruebas.

## Marco Teórico

### Python

Python es un lenguaje de programación popular y de alto nivel. Es conocido por su sintaxis clara y legible, lo que facilita escribir y entender código. Python es versátil y se utiliza en una variedad de campos, como desarrollo web, inteligencia artificial, análisis de datos y automatización de tareas.

Una de las fortalezas de Python es su comunidad activa y amplia biblioteca estándar, que proporciona una amplia gama de módulos y paquetes para facilitar el desarrollo de aplicaciones. Es un lenguaje interpretado, lo que significa que no requiere un paso adicional de compilación y es fácil de aprender para principiantes, pero también poderoso y flexible para proyectos más avanzados.

### OpenCV

OpenCV es un "kit de herramientas" para trabajar con imágenes y videos en una computadora. Ayuda a detectar objetos, seguir movimientos o reconocer caras en fotos y videos. Es muy popular porque es fácil de usar y tiene muchas funciones útiles.

### Haar Cascades 

Es una herramienta para encontrar objetos específicos en imágenes, como por ejemplo, rostros. Funciona entrenando a la computadora con ejemplos de imágenes que tienen rostros y otras que no. Después de ese entrenamiento, la computadora puede buscar rostros en nuevas imágenes.

[ver más detalles](https://github.com/jorferr89/reconocimiento-rostro-ia/blob/main/anexos/HaarCascades-RodriguezJorgeFernando.pdf)

### Local Binary Patterns Histograms (LBPH)

El método LBPH es una forma de enseñar a una computadora a reconocer caras en imágenes. En lugar de mirar los colores de la imagen, LBPH se enfoca en los patrones pequeños y detalles, como las texturas en la cara. Divide la cara en pedazos pequeños y comparas cómo se ven esos pedazos. Luego, se utiliza esta información para decirle a la computadora cómo es la cara de alguien. Es una forma efectiva de hacer que una computadora aprenda a reconocer rostros en fotos.

Es más robusto ante cambios de iluminación. La idea es no mirar la imagen completa como un vector de alta dimensión, sino describir solo las características locales de un objeto. 

Algunas consideraciones: 
* Las imágenes de entrenamiento como de predicción deben estar en escala de grises. 
* No se tiene especificaciones sobre el tamaño de las imágenes correspondientes a los rostros.

[ver más detalles](https://github.com/jorferr89/reconocimiento-rostro-ia/blob/main/anexos/LBPH-RodriguezJorgeFernando.pdf)

## Creación de la Base de datos con los rostros

Para la realización del reconocimiento facial se necesiraán los rostros de las personas que deseemos reconocer. Es recomendable que se realice la recolección de estas imágenes en el escenario o ambiente en donde se vaya a aplicar el reconocimiento facial, tener en cuenta variaciones de condiciones de luz, que las personas lleven o que no lentes, incluso que cierren o guiñen un ojo. Toda esta variedad de imágenes que se obtenga de los rostros contribuirá al desempeño del algoritmo.

[ver código](https://github.com/jorferr89/reconocimiento-rostro-ia/blob/main/capturaRostro.py)

### Prueba

![Captura Rostro](/capturasDePantalla/captura-rostro.jpg)

## Preparación de los datos, Entrenamiento y Almacenamiento del Modelo

Antes de proceder con el entrenamiento es necesario asociar una etiqueta a cada persona (entrenamiento supervisado). Ejemplo: cuando leamos la carpeta ‘Persona 1’ todas esas imágenes se les asignará etiqueta 0, luego a todas imágenes de los rostros de ‘Persona 2’ se asignará 1,  de ‘Persona 3’ se asignará 2, y así sucesivamente. Con cada etiqueta la computadora sabrá que las imágenes pertenecen a personas distintas. El código está preparado para entrenarlo con más de una persona, pero las pruebas serán realizadas para que me reconozca unicamente a mí.

Una vez entrenado el modelo, se lo puede almacenar. ¿Para qué nos sirve? Para leerlo en otro script, y nos ahorramos de volver a entrenarlo.

[ver código](https://github.com/jorferr89/reconocimiento-rostro-ia/blob/main/entrenamientoLBPH.py)

### Prueba

![Entrenamiento](/capturasDePantalla/entrenamiento.jpg)

## Reconocimiento

[ver código](https://github.com/jorferr89/reconocimiento-rostro-ia/blob/main/reconocimientoFacial.py)

### Prueba

![Captura Rostro](/capturasDePantalla/reconocimiento-jorge.jpg)

![Captura Rostro](/capturasDePantalla/reconocimiento-desconocido.jpg)

## Conclusión

El reconocimiento facial mediante el uso de Python, OpenCV y el método Local Binary Patterns Histograms (LBPH) ofrece una solución efectiva y eficiente para identificar rostros en imágenes. Esta técnica proporciona una representación robusta de las texturas faciales, lo que resulta en un sistema preciso y rápido.

Como posible investigación futura, se podría explorar la implementación de este proyecto con una ESP32-CAM. La combinación de la ESP32-CAM con el código Python desarrollado para el reconocimiento facial brinda la oportunidad de construir sistemas compactos y autónomos, los cuales pueden integrarse en diversas aplicaciones, como la seguridad en el hogar, el control de acceso o incluso la automatización de procesos.

## Bibliografía

* DETECCIÓN DE ROSTROS con Haar Cascades Python – OpenCV. Youtube. Recuperado de: https://www.youtube.com/watch?v=J1jlm-I1cTs [03/01/2024].
* Reconocimiento Facial | Python - OpenCV. Youtube. Recuperado de: https://www.youtube.com/watch?v=cZkpaL36fW4 [03/01/2024].
* OpenCV - Face Recognition with OpenCV. OpenCV. Recuperado de: https://docs.opencv.org/4.2.0/da/d60/tutorial_face_main.html [03/01/2024].
* OpenCV - cv::face::LBPHFaceRecognizer Class Reference. Recuperado de: https://docs.opencv.org/3.4/df/d25/classcv_1_1face_1_1LBPHFaceRecognizer.html [04/01/2024].
* Consultas a ChatGPT. Recuperado de: https://openai.com/blog/chatgpt [05/01/2024].
* Comprendiendo el reconocimiento facial mediante el algoritmo LBPH. Analytics Vidhya. Recuperado de: https://www.analyticsvidhya.com/blog/2021/07/understanding-face-recognition-using-lbph-algorithm/ [06/01/2024].