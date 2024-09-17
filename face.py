#importing opencv and system
import cv2
import sys

#initial setup variables, getting paramaters passed trhough, setting the cascase
#and starting video capture
casPath = sys.argv[1]
faceCas = cv2.CascadeClassifier(casPath)
camera = cv2.VideoCapture(0)

#ret is the video frame that is taken in, and frame is the code returned
while true:
    ret, frame = camera.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BAYER_BG2GRAY)
    faces = faceCas.detectMultiScale(
    gray,
    scaleFactor=1.2,
    minNeighbors=5,
    minSize=(30,30),
    flags=cv2.cv.CV_HAAR_SCALE_IMAGE
    )
    cv2.