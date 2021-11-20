from PIL import Image

import face_recognition

image = face_recognition.load_image_file("DIK_8499.JPG")

face_locations = face_recognition.face_locations("PP.JPG")


for face in face_locations:
    top, right, bottom, left = face
    face_image = image [top:bottom, left:right]
    pil_image = Image.fromarray(face_image)
    pil_image.show()

