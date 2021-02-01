import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import random as rng
import cv2
import os
import glob 
import pandas as pd
%matplotlib inline

def canny(selected_image):
    image = cv2.cvtColor(selected_image, cv2.COLOR_BGR2RGB)
    gray = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
    #plt.imshow(gray)
    cv2.imwrite('B1.jpg',gray)

    retval, binary = cv2.threshold(gray,90, 255,0)
    #plt.imshow(binary, cmap='gray')
    cv2.imwrite('B2.jpg',binary)

    edged = cv2.Canny(gray ,15,180) 
    #plt.imshow(edged, cmap='gray')
    cv2.imwrite('B3.jpg',edged)
    return(binary,edged)
  
  def contourrr(image,binary):
    #retval, contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours, hierarchy = cv2.findContours(binary,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    # Draw all contours on a copy of the original image
    contours_image = np.copy(image)
    print(len(contours))

    contours_image = cv2.drawContours(contours_image, contours, -1, (0,0,255), 3)

    #plt.imshow(contours_image)
    cv2.imwrite('B5.jpg',contours_image)
    return(contours)
  
  def roi(image,im_binary,contours,ROI_number):
    global roi1,roi2
    for c in contours:
        x,y,w,h = cv2.boundingRect(c)
        #print(cv2.contourArea(c))
        z = cv2.contourArea(c) 
        if(z>300000 and z<400000):
            print('--')
            print(cv2.contourArea(c))
            img = cv2.rectangle(image,(x-30,y-30),(x+w+30,y+h+30),(0,255,0),3)
            roi1 = im_binary[y-30:y+h+30,x-30:x+w+30]
            #cv2.imwrite('B1000.jpg',roi1)
        elif(z>80000 and z<300000):
            print('--')
            print(cv2.contourArea(c))
            img = cv2.rectangle(image,(x-20,y-20),(x+w+20,y+h+20),(0,255,0),3)
            roi2 = im_binary[y-20:y+h+20,x-20:x+w+20]
            #cv2.imwrite('B1011.jpg',roi2)
    
    cv2.imwrite("0,1/Color_image"+str(ROI_number)+".jpg",img)
    
    #print('*')
    print(ROI_number)




    #plt.imshow(img,cmap='gray')
    #cv2.imwrite('B6.jpg',img)
    return(roi1,roi2,img)

