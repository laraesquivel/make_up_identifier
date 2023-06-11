import cv2 as cv
from pathlib import Path
import os
from random import randint
import numpy as np
import sys


LOWER_SKIN = np.array([0, 20, 70], dtype=np.uint8)
UPPER_SKIN = np.array([20, 255, 255], dtype=np.uint8)

class Face_Detect:
    def __init__(self,in_path,user=f'{randint(0,sys.maxsize)}',cascade_classifier="modelos/haarcascade_frontalface_default.xml",out_path="img_cortadas"):
        self.__in_path = in_path
        self.out_path = out_path
        self.id = user
        self.img = cv.imread(self.__in_path)
        self.cascade_classifier = cv.CascadeClassifier(cascade_classifier)

        if not os.path.exists(out_path):
            os.makedirs(out_path)
    
    def detect(self):
        gray = cv.cvtColor(self.img,cv.COLOR_BGR2GRAY)
        faces = self.cascade_classifier.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        
        for (x, y, w, h) in faces:
            roi_color = self.img[y:y+h, x:x+w]
            filename = f'{self.id}.jpg'
            path = os.path.join(self.out_path,filename)
            cv.imwrite(path, roi_color)
        return path

   
    
    def clear():
        pass

