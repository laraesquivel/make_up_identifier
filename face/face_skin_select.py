import numpy as np
import cv2 as cv
import colorsys
from random import randint
import sys
import os

class Face_Skin_Select_Color:
    LOWER_SKIN = np.array([0, 40, 30], dtype=np.uint8)
    UPPER_SKIN = np.array([20, 255, 255], dtype=np.uint8)

    def __init__(self, origin_path):
        self.origin_path = origin_path
        self.image = None
        self.out_path = "img_detect"
        self.path = None
        try:
            self.image = cv.imread(self.origin_path)
            self.image_hsv = cv.cvtColor(self.image, cv.COLOR_BGR2HSV)
        except Exception as e:
            print(e)
        if not os.path.exists(self.out_path):
            os.makedirs(self.out_path)
        skin_mask = cv.inRange(self.image_hsv, Face_Skin_Select_Color.LOWER_SKIN, Face_Skin_Select_Color.UPPER_SKIN)
        self.skin_image = cv.bitwise_and(self.image, self.image, mask=skin_mask)
    
    def select(self):
        bbox = cv.selectROI(self.skin_image)
        regiao = self.skin_image[int(bbox[1]):int(bbox[1]+bbox[3]), int(bbox[0]):int(bbox[0]+bbox[2])]
        self.skin_image = regiao
        filename = f'{(randint(0,sys.maxsize))}.jpg'
        self.path = os.path.join(self.out_path,filename)
        cv.imwrite(self.path,self.skin_image)
        cv.imshow('Região Extraída', regiao)
        cv.waitKey(0)
        cv.destroyAllWindows()

    def count_color(self):
        imagem_hsv = self.skin_image
        altura, largura, _ = imagem_hsv.shape

    # Inicializar o dicionário para armazenar as contagens de cada cor
        contagem_cores = {}

    # Iterar sobre cada pixel da imagem
        for y in range(altura):
            for x in range(largura):
                # Obter o valor do pixel no espaço de cores HSV
                h, s, v = imagem_hsv[y, x]

                # Verificar se a cor já está no dicionário
                if (h, s, v) in contagem_cores:
                    # Incrementar a contagem para essa cor
                    contagem_cores[(h, s, v)] += 1
                else:
                    # Iniciar a contagem para essa cor
                    contagem_cores[(h, s, v)] += 1

        # Imprimir a contagem para cada cor
        for cor, contagem in contagem_cores.items():
            print('Cor:', cor)
            print('Contagem:', contagem)
            print('---')


    def mean_color(self):
        imagem_hsv = self.skin_image
        mask_preto = cv.inRange(imagem_hsv, (0, 0, 0), (179, 255, 10))
        pixels_nao_pretos = cv.bitwise_and(imagem_hsv, imagem_hsv, mask=~mask_preto)
        #tom_medio_hsv = np.mean(pixels_nao_pretos)
        #tom_medio_hsv = circular_mean(pixels_nao_pretos,axis=(0,1))
        pixels_rgb = cv.cvtColor(pixels_nao_pretos, cv.COLOR_HSV2RGB)
        r_mean = np.mean(pixels_rgb[:,0])
        g_mean = np.mean(pixels_rgb[:,1])
        b_mean = np.mean(pixels_rgb[:,2])
        h, s, v = colorsys.rgb_to_hsv(r_mean/255,g_mean/255,b_mean/255)
        h = int(h * 360)
        s = int(s * 255)
        v = int(v * 255)
        tom_medio_hsv = (h,s,v)

        
        print("Tom Médio em HSV:", tom_medio_hsv)
        return tom_medio_hsv


