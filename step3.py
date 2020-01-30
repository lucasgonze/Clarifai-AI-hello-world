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

last_status = None
try:
    while True:

        # Capture frame-by-frame
        ret, frame = cap.read()
        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        cv.imwrite("lastframe.jpg", frame	)

        # run Clarifai predictions
        response = model.predict_by_filename("lastframe.jpg")

        # Glasses detected?
        concepts = response['outputs'][0]['data']['concepts']
        new_status=False
        for concept in concepts:
            if concept['name'] == u'eyeglasses':
                new_status=True

        # Best UX ever
        if new_status != last_status:
            if new_status:
                print "four eyes"
            else:
                print "two eyes"
            last_status = new_status

except KeyboardInterrupt:
    cap.release()
