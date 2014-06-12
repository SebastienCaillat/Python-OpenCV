#!python2
""" Simple example of video manipulation with OpenCV
inspired from:
http://docs.opencv.org/trunk/doc/py_tutorials/py_gui/py_video_display/py_video_display.html
http://docs.opencv.org/trunk/doc/py_tutorials/py_imgproc/py_colorspaces/py_colorspaces.html
https://stackoverflow.com/questions/22903870/get-value-from-detect-colour-python-opencv
http://wiki.labomedia.org/index.php/OpenCV_pour_Python

Last update S. Caillat 13/06/2014"""
import numpy as np
import cv2
# Define lower & upper level for image threshold
lower_level = np.array([100,100,100],dtype=np.uint8)
upper_level = np.array([179,255,255],dtype=np.uint8)    

cap = cv2.VideoCapture(0)
print ('Press q to quit')

while True :
    ret,frame = cap.read()     # Capture frame-by-frame
    # Convert BGR (Blue Green, Red) to HSV (Hue, Saturation, Value)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # Threshold the HSV image in the selected range
    mask = cv2.inRange(frame,lower_level,upper_level)
    # Convert frame from color to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # height, width = frame.shape[:2] # Find image size
    # Display the resulting frame
    cv2.imshow('Color',frame)
    cv2.imshow('B&W',gray)
    cv2.imshow('Mask',mask)
    if cv2.waitKey(1) & 0xFF == ord('q'): break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
