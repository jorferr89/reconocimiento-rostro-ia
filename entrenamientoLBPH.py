import cv2
import os
import numpy as np

# Ruta donde se encuentran los datos de entrenamiento
dataPath = 'D:/INTEGRADOR-IA/datos'

# Lista de personas en el conjunto de datos
peopleList = os.listdir(dataPath)
print('Lista de personas: ', peopleList)

# Listas para almacenar etiquetas y datos de rostros
labels = []
facesData = []

# Inicializar la etiqueta
label = 0

# Iterar sobre las personas en el conjunto de datos
for nameDir in peopleList:
    # Ruta completa a la carpeta de la persona
    personPath = dataPath + '/' + nameDir
    print('Leyendo las imágenes...')

    # Iterar sobre los archivos en la carpeta de la persona
    for fileName in os.listdir(personPath):
        print('Rostros: ', nameDir + '/' + fileName)
        
        # Agregar la etiqueta correspondiente a la lista de etiquetas
        labels.append(label)
        
        # Leer la imagen en escala de grises y agregarla a la lista de datos de rostros
        facesData.append(cv2.imread(personPath+'/'+fileName, 0))

    # Incrementar la etiqueta para la próxima persona
    label = label + 1

# Crear un reconocedor de rostros LBPH
face_recognizer = cv2.face.LBPHFaceRecognizer_create()

# Entrenar el reconocedor con los datos recopilados
print("Entrenando...")
face_recognizer.train(facesData, np.array(labels))

# Guardar el modelo entrenado en un archivo XML
face_recognizer.write('modeloLBPHFace.xml')
print("Modelo almacenado")