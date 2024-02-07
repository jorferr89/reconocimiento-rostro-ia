# Importando OpenCV
import cv2
# Importando el archivo XML de HAAR CASCADE
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# Cargando la imagen de prueba
img = cv2.imread('test.jpg')

# Redimensionando el frame
width = int(img.shape[1] * 0.5)
height = int(img.shape[0] * 0.5)
dim = (width, height)
img_resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

# Convirtiendo la imagen a escala de grises
gray = cv2.cvtColor(img_resized, cv2.COLOR_BGR2GRAY)
# Permitiendo la detección a múltiples escalas (múltiples tamaños)
faces = face_cascade.detectMultiScale(gray, 1.1, 6)
# Creando un rectángulo alrededor de la cara detectada
for (x, y, w, h) in faces:
    cv2.rectangle(img_resized, (x, y), (x+w, y+h), (0, 0, 250), 2)
# Mostrando la imagen
cv2.imshow('Rostros detectados', img_resized)
# Esperando la tecla de escape para cerrar la imagen
cv2.waitKey()