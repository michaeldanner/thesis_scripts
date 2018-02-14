# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 20:02:01 2017

@author: Michael
"""

import cv2
import os, glob
from shutil import copyfile

#OUTPUTBASE = 'E:/300VW_Dataset_2015_12_14/404/'
OUTPUTBASE = 'E:/300VW_Marco/509/'

outputfolder = OUTPUTBASE +"/landmarks/"
if (not os.path.exists(outputfolder)):
    os.mkdir(outputfolder)
    print('Make directory: ' + outputfolder)

lms = glob.glob(OUTPUTBASE+"/annot/*.pts")
count = 1
print(str(len(lms)))
for lm in lms:
    if count%50==0:
        print(str(count))
        dst = lm.replace('annot', 'landmarks')
        copyfile(lm, dst)
    count += 1
quit()


if (not os.path.isdir(OUTPUTBASE)):
    print(OUTPUTBASE + " is not a valid directory!")
    quit(1)

vidcap = cv2.VideoCapture(OUTPUTBASE + '/vid.avi')
success,image = vidcap.read()
count = 1
outputfolder = OUTPUTBASE +"/frames/"

if (not os.path.exists(outputfolder)):
    os.mkdir(outputfolder)
    print('Make directory: ' + outputfolder)

print('Start creating frames from video')

while success:
  success,image = vidcap.read()
  if count%50==0:
      #print(' - create frame id ' + str(count))
      cv2.imwrite(outputfolder + "/%06d.png" % count, image)     # save frame as JPEG file
  if cv2.waitKey(10) == 27:                     # exit if Escape is hit
      break
  count += 1