# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 20:02:01 2017

@author: Michael
"""

import cv2
import os, glob


OUTPUTBASE = 'E:/300VW_Dataset_2015_12_14/028/'

outputfolder = OUTPUTBASE +"/landmarks/"

keyframes = ""


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
  print(' - create frame id ' + str(count))
  cv2.imwrite(outputfolder + "/%06d.png" % count, image)     # save frame as JPEG file

  if cv2.waitKey(10) == 27:                     # exit if Escape is hit
      break
  count += 1

