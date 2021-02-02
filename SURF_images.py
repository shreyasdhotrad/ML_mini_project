import os
import matplotlib.pyplot as plt
import cv2

yoke_dir="G:\yoke images"
parent="G:/"
dir="SURF_images"

path=os.path.join(parent,dir)
#os.mkdir(path)
for img in os.listdir(yoke_dir):
    imgpath=os.path.join(yoke_dir,img)
    yoke_image=cv2.imread(imgpath)

    gray = cv2.cvtColor(yoke_image, cv2.COLOR_BGR2GRAY) 
    edged = cv2.Canny(gray, 30, 150)

    surf=cv2.xfeatures2d.SURF_create(2000)
    kp, des = surf.detectAndCompute(edged,None)
    img2 = cv2.drawKeypoints(yoke_image,kp,None,(255,0,0),4)
    plt.imshow(img2,cmap='gray'),plt.show()

    fullOutPath = os.path.join(path,img) 
    #cv2.imwrite(fullOutPath,img2)