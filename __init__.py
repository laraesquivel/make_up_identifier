from face.face_detect import Face_Detect
from face.face_skin_color import Face_Skin_Color

F = Face_Detect("exemplos_test/black.jpg")
path = F.detect()
print(path)
A = Face_Skin_Color(path)
A.mean_color()
