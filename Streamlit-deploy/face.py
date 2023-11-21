import cv2
import imutils
import numpy as np
import urllib.request
from PIL import Image, ImageDraw
from IPython.display import display
import face_recognition

face_1 = face_recognition.load_image_file("E:/Void - Hack/face-recognition/pro-pic.jpeg")
face_1_encoding = face_recognition.face_encodings(face_1)[0]


known_face_encodings = [
    face_1_encoding
    
]
known_face_names = [
    "mubeen"
   
]
print("Done learning and creating profiles")

file_name ='E:/Void - Hack/face-recognition/myself.jpeg'
unknown_image = face_recognition.load_image_file(file_name)
unknown_image_to_draw = cv2.imread(file_name)

face_locations = face_recognition.face_locations(unknown_image)
face_encodings = face_recognition.face_encodings(unknown_image, face_locations)

pil_image = Image.fromarray(unknown_image)
draw = ImageDraw.Draw(pil_image)

for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    # See if the face is a match for the known face(s)
    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

    name = "Unknown"

    face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
    best_match_index = np.argmin(face_distances)
    if matches[best_match_index]:
        name = known_face_names[best_match_index]

    # Draw a box around the face using the Pillow module
    cv2.rectangle(unknown_image_to_draw,(left, top), (right, bottom), (0,255,0),3 )
    draw.rectangle(((left, top), (right, bottom)), outline=(0, 255, 255))
    cv2.putText(unknown_image_to_draw,name,(left,top-20), cv2.FONT_HERSHEY_SIMPLEX,1, (0,0,255), 2,cv2.LINE_AA)
    print(name)
    # makeEntry(name)

# display(pil_image)
cv2.imshow("output",unknown_image_to_draw)
cv2.waitKey(0)
cv2.destroyAllWindows()  # Close all windows
