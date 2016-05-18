# vision_test_1 - created by Akilesh Praveen
# May 15
# www.github.com/akipraveen

'''
This is a simple opencv image trial in which minimal edits upon an image
are performed. There is no actual goal of this program other than testing
the editing abilities of OpenCV. It's simply a trial run of sorts.
'''

import cv2

# load an image
img_raw = cv2.imread('resources/facial_profiles/1.jpg')

# change bgr image to rgb
img = cv2.cvtColor(img_raw, cv2.COLOR_BGR2RGB)

# get the pixel at 100, 100
px = img[100,100]
px = [255,255,255]
print px

# testing a loop to change the color of an entire block of an image (with for loops)
for x in range(0,100):
    for y in range(0,100):
        # color 100x100 block in red color
        img[x][y] = [0,0,255]


# saving the image that we edited to a new image file
cv2.imwrite("resources/facial_profiles/1_modified.jpg", img)

# finally, show the image after loading it
cv2.namedWindow("Modified image", cv2.WINDOW_AUTOSIZE)
# display image for 2s before destroying it.
cv2.imshow("Modified image", img)
cv2.waitKey(1000)
cv2.destroyAllWindows()




