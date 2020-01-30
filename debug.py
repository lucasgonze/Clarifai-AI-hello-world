import numpy as np
import cv2 as cv
from clarifai.rest import ClarifaiApp

cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

app = ClarifaiApp(api_key='f805f0ec701747a2ae4db700dd78f217')
model = app.public_models.general_model

print "Running. Press control+C to quit."
try:
    while True:
        print "hi"
 except Exception as e:
     print e
     cap.release()
