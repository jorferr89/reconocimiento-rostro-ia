import cv2
import os
import imutils

# Nombre de la persona para la que se capturarán los rostros
personName = 'Jorge'

# Ruta donde se guardarán los datos
dataPath = 'ruta/datos'
personPath = dataPath + '/' + personName

# Verificar si la carpeta para la persona existe, si no, crearla
if not os.path.exists(personPath):
    print('Carpeta creada:', personPath)
    os.makedirs(personPath)

# Configurar la captura de video desde la cámara o un archivo de video
# cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap = cv2.VideoCapture('ruta/archivo/video/captura.mp4')

# Cargar el clasificador de cascada para la detección de rostros
faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Inicializar el contador de rostros capturados
count = 0

# Bucle principal para capturar rostros
while True:
    # Leer un fotograma desde la cámara o archivo de video
    ret, frame = cap.read()
    if ret == False:
        break

    # Redimensionar el fotograma
    scale_percent = 50
    width = int(frame.shape[1] * scale_percent / 100)
    height = int(frame.shape[0] * scale_percent / 100)
    dim = (width, height)
    frame = cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)

    # Convertir el fotograma a escala de grises para la detección de rostros
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    auxFrame = frame.copy()

    # Detectar rostros en la imagen
    faces = faceClassif.detectMultiScale(gray, 1.3, 5)

    # Iterar sobre las caras detectadas
    for (x, y, w, h) in faces:
        # Dibujar un rectángulo verde alrededor de la cara
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Recortar el rostro de la imagen original
        rostro = auxFrame[y:y+h, x:x+w]

        # Redimensionar el rostro a 150x150 píxeles
        rostro = cv2.resize(rostro, (150, 150), interpolation=cv2.INTER_CUBIC)

        # Guardar el rostro como una imagen en la carpeta correspondiente
        cv2.imwrite(personPath + '/rostro_{}.jpg'.format(count), rostro)
        count = count + 1

    # Mostrar el fotograma con los rectángulos dibujados
    cv2.imshow('frame', frame)

    # Esperar una tecla (1 milisegundo) y verificar si se presionó 'Esc' o se capturaron más de 300 rostros
    k = cv2.waitKey(1)
    if k == 27 or count >= 600:
        break

# Liberar la captura de video y cerrar las ventanas de OpenCV
cap.release()
cv2.destroyAllWindows()