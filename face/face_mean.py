import cv2 as cv
import colorsys
import numpy as np

class Face_mean:
    def __init__(self,path):
        self.path = path
        self.image = None
        self.media_bgr = None
        self.media_hsv = None
        try:
            self.image = cv.imread(self.path)
            self.media_bgr =  tuple(np.array(cv.mean(self.image), dtype=np.uint8))
            print(f'Media BGR {self.media_bgr}')
          

            
        except:
            print("Nao foi possivel abrir")
        
        
    def convert_to_hsv(self):
        r = self.media_bgr[2]
        g = self.media_bgr[1]
        b = self.media_bgr[0]
        
        r /= 255.0
        g /= 255.0
        b /= 255.0
        h, s, v = colorsys.rgb_to_hsv(r, g, b)
       
        h *= 360.0
        s *= 100.0
        v = 100.0
        print(f'hsv:{h},{s},{v}')
        return (h,s,v)
        