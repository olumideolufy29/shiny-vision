# facial_rec - created by Akilesh Praveen
# May 18
# www.github.com/akipraveen

import cv2
import sys

''' COMMAND LINE ARGUMENTS
path_to_img = sys.argv[1]
path_to_casc = sys.argv[2]
'''
path_to_img = 'resources/facial_profiles/1.jpg'
path_to_casc = ''

faceCascade = cv2.CascadeClassifier(path_to_casc)

print path_to_img

# Reading the image file
img = cv2.imread(path_to_img)
exit()
# Create a gray version of the Image
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detecting the faces
faces = faceCascade.detectMultiScale(
    img_gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
    flags = cv2.cv.CV_HAAR_SCALE_IMAGE
)