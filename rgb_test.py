# rgb_test - created by Akilesh Praveen
# May 17
# www.github.com/akipraveen

import cv2
import numpy as np

# debug boolean, change to True to view debug messages
isDebug = True

# Read the image as input
img = cv2.imread('resources/colored_squares/green.png')

# Get image dimensions
height, width, channel = img.shape
if (isDebug): print img.shape

# Create three lists to gauge the Blue, Green and Red
blue = []
red = []
green = []

# for loop to parse through every pixel in the image
for i in range(0, height-1):
    for j in range (0, width-1):
        px = img[i, j]
        if (isDebug): print "blue:", px[0], " red:", px[1], " green:", px[2], '\n'
        # add all pixels to a List
        blue.append(px[0])
        green.append(px[1])
        red.append(px[2])

# function that adds all items in a list.
def listsum(numList):
    sum=0
    for i in numList:
        sum+=i
    return sum


# Print total
if (isDebug):
    print "blue color units> ", listsum(blue)
    print "green color units> ", listsum(green)
    print "red color units> ", listsum(red), '\n'

total=listsum(blue)+listsum(green)+listsum(red)
print '\n', "Analysis Results:"
print 'BLUE> ', np.true_divide(listsum(blue)*100, total), '%'
print 'GREEN> ', np.true_divide(listsum(green)*100, total), '%'
print 'RED> ', np.true_divide(listsum(red), total)*100, '%'