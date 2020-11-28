import cv2
import numpy as np
import glob
import os

img_array = []
sortDirImgs = sorted(glob.glob('results/first3000-5154/*jpg'))
#size=(30,30)
i = 0
for filename in sortDirImgs:
    img = cv2.imread(filename)
    height, width, layer = img.shape
    size = (width,height)
    img_array.append(img)
    print("%d",i)
    i = i + 1
out = cv2.VideoWriter('videFish.avi',cv2.VideoWriter_fourcc(*'DIVX'),60, size)

for i in range(len(img_array)):
    out.write(img_array[i])
out.release()
