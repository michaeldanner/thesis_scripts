# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 20:53:18 2017

@author: Michael
"""

import cv2

OUTPUTBASE = 'E:/300VW_Dataset_2015_12_14/512/'

count = 1
img1 = cv2.imread(OUTPUTBASE + "/vid/%06d.png.isomap.png" % count)
height , width , layers =  img1.shape
print(height)
print(width)
vidwrite = cv2.VideoWriter(OUTPUTBASE + '/out_vid.avi', -1, 20, (width,height))

while count < 500:
    image = cv2.imread(OUTPUTBASE + "/vid/%06d.png.isomap.png" % count)
    vidwrite.write(image)
    count += 1
    
cv2.destroyAllWindows()
vidwrite.release()