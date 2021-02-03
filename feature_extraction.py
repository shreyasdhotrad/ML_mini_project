import cv2 
import numpy as np 
import matplotlib.pyplot as plt
from skimage.io import imread, imshow
from skimage.transform import resize
from skimage.feature import hog
from skimage import exposure

img=cv2.imread("G:\yoke images\Black Spot-1.jpg")

############### CANNY ###############################
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
edged = cv2.Canny(gray, 30, 150)

############### CONTOUR ###############################
_,contours, hierarchy = cv2.findContours(edged,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
cv2.drawContours(img, contours, -1, (0,255, 0), 3)  
for i in contours:
  x,y,w,h=cv2.boundingRect(i)
  image=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

############### SURF ###############################
surf=cv2.xfeatures2d.SURF_create(2000)
kp, des = surf.detectAndCompute(edged,None)
image = cv2.drawKeypoints(image,kp,None,(0,0,255),4)

############### SIFT ###############################
sift=cv2.xfeatures2d.SIFT_create(2000)
kp = sift.detect(edged,None)
image = cv2.drawKeypoints(image,kp,None,(255,0,0),4)

plt.axis("off")
plt.imshow(image)
plt.show()
