import cv2
import numpy as np

# Carregar o arquivo de imagem
image_path = 'teste/img.jpg'
image = cv2.imread(image_path)

# Carregar o classificador pré-treinado para detecção de rosto
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Converter a imagem para escala de cinza
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Realizar a detecção de rosto na imagem
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Criar uma máscara preta do mesmo tamanho da imagem
mask = np.zeros_like(image)

# Preencher a região fora dos rostos detectados na máscara com a cor preta
for (x, y, w, h) in faces:
    cv2.rectangle(mask, (x, y), (x+w, y+h), (255, 255, 255), -1)

# Aplicar a máscara na imagem original
result = cv2.bitwise_and(image, mask)

# Mostrar a imagem com apenas o rosto detectado
cv2.imshow('Apenas o Rosto', result)
cv2.waitKey(0)
cv2.destroyAllWindows()


