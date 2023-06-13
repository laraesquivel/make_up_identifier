from face.face_detect import Face_Detect
from face.face_skin_color import Face_Skin_Color
from utils.convert import distancia_eucliana

F = Face_Detect("exemplos_test/face.jpg")
path = F.detect()
print(path)
A = Face_Skin_Color(path)
tom = A.mean_color()
print(distancia_eucliana(tom))
