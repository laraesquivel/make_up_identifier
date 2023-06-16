from face.face_detect import Face_Detect
from face.face_skin_color import Face_Skin_Color
from face.face_skin_select import Face_Skin_Select_Color
from utils.convert import distancia_eucliana

F = Face_Detect("exemplos_test/461777879.webp")
path = F.detect()
print(path)

A = Face_Skin_Select_Color(path)
A.select()
color = A.mean_color()
print(distancia_eucliana(color))

#A = Face_Skin_Color(path)
#tom = A.mean_color()
#print(distancia_eucliana(tom))
#print(type(distancia_eucliana(tom)))