import os
import matplotlib.pyplot as plt
import cv2

yoke_dir="G:\yoke images"
parent="G:/"
dir="CONTOUR_images"

path=os.path.join(parent,dir)
#os.mkdir(path)
for img in os.listdir(yoke_dir):
    imgpath=os.path.join(yoke_dir,img)
    yoke_image=cv2.imread(imgpath)

    gray = cv2.cvtColor(yoke_image, cv2.COLOR_BGR2GRAY) 
    edged = cv2.Canny(gray, 30, 150)

    _,contours, hierarchy = cv2.findContours(edged,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(yoke_image, contours, -1, (255,0, 0), 3)  
    for i in contours:
        x,y,w,h=cv2.boundingRect(i)
        image=cv2.rectangle(yoke_image,(x,y),(x+w,y+h),(0,0,255),2)
    
    plt.imshow(image,cmap='gray'),plt.show()
    fullOutPath = os.path.join(path,img) 
    c#v2.imwrite(fullOutPath,image)