from skimage.io import imread, imshow
from skimage.transform import resize
from skimage.feature import hog
from skimage import exposure
import matplotlib.pyplot as plt
import cv2
import os

yoke_dir="G:\yoke images"
parent="G:/"
dir="HOG_images"

path=os.path.join(parent,dir)
os.mkdir(path)
for img in os.listdir(yoke_dir):
    imgpath=os.path.join(yoke_dir,img)
    yoke_image=cv2.imread(imgpath)

    resized_img=resize(yoke_image,(128*4,64*4))
    fd,hog_image=hog(resized_img,orientations=9,pixels_per_cell=(8,8),cells_per_block=(2,2),visualize=True,multichannel=True)
    final=cv2.convertScaleAbs(hog_image,alpha=(255.0))

    fullOutPath = os.path.join(path,img) 
    cv2.imwrite(fullOutPath,final)