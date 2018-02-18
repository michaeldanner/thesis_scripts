#!/usr/bin/env python3.5

import glob, os
import eos_starter_lib as esl
from concurrent.futures import ThreadPoolExecutor

EXE = "D:/Daten/Projects/eosbuild/examples/Release/fit-model.exe"

LOGNAME = "fitting.log"

OUTPUTBASE = "D:/CASIA/multi_fit_CCR_iter75_reg30_256/"

message = None

with ThreadPoolExecutor(max_workers=6) as executor:
    id_folders = glob.glob("E:/300VW_Dataset_2015_12_14/028*")
    for n in range(0,len(id_folders)):
        print(len(id_folders))
        id_folder = id_folders[n]
        try:
            id_folder = os.path.abspath(id_folder)	
            id_num = os.path.basename(id_folder)
            message = "video " + id_num + "   (" + str(n) + " of " + str(len(id_folders)) + " )"
            # check if it's a folder
            # if (not os.path.isdir(id_folder)):
            # continue;


			# gather lm and img files
            #lms  = glob.glob(id_folder+"/annot/*.pts")
            imgs = glob.glob(id_folder+"/frames/*.png")
            if (not os.path.exists(id_folder+"/out/")):
                os.mkdir(id_folder+"/out/")
                print('Make directory: ' + id_folder)
            for img in imgs:
                lm = img.replace('frames','annot').replace('png','pts')
                #print (lm)
                outputfolder = img.replace('frames','out')
                #print (outputfolder)
                m = message + " - (" + str(img) + " of " + str(len(imgs)) + " )"
                cmd = esl.assemble_command(EXE, lm, img, outputfolder)
                cmd = cmd.replace("\\", "/")
                print (cmd)
			
                executor.submit(esl.start_and_log,"multiframe fitting on "+m, cmd, None, log=outputfolder+LOGNAME) #21600
                
        except Exception as e:
            print("ERROR on " + message + ": " + str(e))
            