import cv2
import os

# Ruta donde se encuentran los datos
dataPath = 'D:/INTEGRADOR-IA/datos'
# Obtener la lista de imágenes en el directorio
imagePaths = os.listdir(dataPath)

# Crear el reconocedor de rostros LBPH y cargar el modelo entrenado
face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read('modeloLBPHFace.xml')

# Configurar la captura de video desde un archivo de video
cap = cv2.VideoCapture('videosPrueba/Jorge-Prueba.mp4')

# Clasificador de cascada para la detección de rostros
faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:
    # Leer un fotograma del video
    ret, frame = cap.read()
    
    # Salir si no se pudo leer el fotograma
    if ret == False:
        break

    # Redimensionar el fotograma
    scale_percent = 50
    width = int(frame.shape[1] * scale_percent / 100)
    height = int(frame.shape[0] * scale_percent / 100)
    dim = (width, height)
    frame = cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)
    
    # Convertir el fotograma a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    auxFrame = gray.copy()

    # Detectar rostros en el fotograma
    faces = faceClassif.detectMultiScale(gray, 1.3, 5)

    # Iterar sobre los rostros detectados
    for (x, y, w, h) in faces:
        # Recortar y redimensionar el rostro
        rostro = auxFrame[y:y+h, x:x+w]
        rostro = cv2.resize(rostro, (150, 150), interpolation=cv2.INTER_CUBIC)

        # Realizar la predicción del rostro
        result = face_recognizer.predict(rostro)

        # Mostrar el ID de la persona y su nombre
        cv2.putText(frame, '{}'.format(result), (x, y-5), 1, 1.3, (255, 255, 0), 1, cv2.LINE_AA)

        # Verificar la confianza de la predicción

        # Si la confianza de la predicción es menor a 70 (umbral de confianza), se considera una predicción válida
        if result[1] < 70:
            cv2.putText(frame, '{}'.format(imagePaths[result[0]]), (x, y-25), 2, 1.1, (0, 255, 0), 1, cv2.LINE_AA)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
         # Si la confianza es mayor o igual a 70, la persona es considerada desconocida
        else:
            cv2.putText(frame, 'Desconocido', (x, y-20), 2, 0.8, (0, 0, 255), 1, cv2.LINE_AA)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

    # Mostrar el fotograma resultante
    cv2.imshow('frame', frame)

    # Esperar la tecla 'Esc' para salir del bucle
    k = cv2.waitKey(1)
    if k == 27:
        break

# Liberar la captura de video y cerrar las ventanas de OpenCV
cap.release()
cv2.destroyAllWindows()