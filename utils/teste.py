# import cv2
# import numpy as np

# import cv2
# import numpy as np

# image_path = 'teste/img.jpg'
# image = cv2.imread(image_path)

# face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# mask = np.zeros_like(image)

# for (x, y, w, h) in faces:
#     cv2.rectangle(mask, (x, y), (x+w, y+h), (255, 255, 255), -1)

# result = cv2.bitwise_and(image, mask)

# imagem = result

# imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

# imagem_suavizada = cv2.GaussianBlur(imagem_cinza, (5, 5), 0)

# _, imagem_binaria = cv2.threshold(imagem_suavizada, 100, 255, cv2.THRESH_BINARY)

# contornos, _ = cv2.findContours(imagem_binaria, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# maior_contorno = max(contornos, key=cv2.contourArea)

# mascara = np.zeros(imagem.shape[:2], dtype=np.uint8)

# cv2.drawContours(mascara, [maior_contorno], -1, (255), thickness=cv2.FILLED)

# imagem_final = cv2.bitwise_and(imagem, imagem, mask=mascara)

# cv2.imshow('Imagem com contorno do rosto', imagem_final)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

import cv2
import numpy as np

imagem = cv2.imread('teste/img.jpg')

imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

imagem_suavizada = cv2.GaussianBlur(imagem_cinza, (5, 5), 0)

gradiente_x = cv2.Sobel(imagem_suavizada, cv2.CV_64F, 1, 0, ksize=3)
gradiente_y = cv2.Sobel(imagem_suavizada, cv2.CV_64F, 0, 1, ksize=3)
gradiente = np.sqrt(gradiente_x ** 2 + gradiente_y ** 2)
gradiente = np.uint8(gradiente)

_, imagem_binaria = cv2.threshold(gradiente, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

contornos, _ = cv2.findContours(imagem_binaria, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

maior_contorno = max(contornos, key=cv2.contourArea)

mascara = np.zeros(imagem.shape[:2], dtype=np.uint8)

cv2.drawContours(mascara, [maior_contorno], -1, (255), thickness=cv2.FILLED)

mascara_invertida = cv2.bitwise_not(mascara)

imagem_final = cv2.bitwise_and(imagem, imagem, mask=mascara_invertida)

cv2.imshow('Imagem com a área em volta da pessoa em preto', imagem_final)
cv2.waitKey(0)
cv2.destroyAllWindows()