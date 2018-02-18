import glob, os
import numpy
from shutil import copyfile

videofolder = "028"
videobase = "E:/300VW_Dataset_2015_12_14"
OUTPUTBASE = 'E:/300VW_Marco/'

videodir =  videobase + "/" + videofolder
outputdir = videodir + "/out"
resultdir = OUTPUTBASE + "/" + videofolder + '/'

id_renders = glob.glob(outputdir + "/*.rendering.json")
count = len(id_renders)
print("count rendering data: " + str(count))

parameter = numpy.matrix([[-1, 0, 0, 0, 0, 99, 99, 99, 99, 99, 99, 99, 99, 99]])
value0 = 0
value1 = 0
value2 = 0
value3 = 0
dist_frontal = 0
i = 0

for id_render in id_renders:
    with open(id_render, "r") as f:
        frame = int(id_render[len(outputdir)+1:id_render.find(".rendering"):1])
        print(frame)
        for read_line in f:

            if ( read_line.find("value0") != -1):
                value0 = float(read_line[22:35:1])
                print("Value0: "+ str(value0))
            if (read_line.find("value1") != -1):
                value1 = float(read_line[22:36:1])
                print("Value1: "+ str(value1))
            if (read_line.find("value2") != -1):
                value2 = float(read_line[22:36:1])
                print("Value2: "+ str(value2))
            if (read_line.find("value3") != -1):
                value3 = float(read_line[22:36:1])
                print("Value3: "+ str(value3))

            dist_frontal = (value1 - 0) ** 2 + (value2 - 0) ** 2 + (value3 - 0) ** 2
            dist_left    = (value1 - 0) ** 2 + (value2 - 0.3) ** 2 + (value3 - 0) ** 2
            dist_right   = (value1 - 0) ** 2 + (value2 + 0.3) ** 2 + (value3 - 0) ** 2
            dist_top     = (value1 + 0.3) ** 2 + (value2 - 0) ** 2 + (value3 - 0) ** 2
            dist_bottom  = (value1 - 0.3) ** 2 + (value2 - 0) ** 2 + (value3 - 0) ** 2
            dist_upleft    = (value1 + 0.2) ** 2 + (value2 - 0.2) ** 2 + (value3 - 0) ** 2
            dist_upright   = (value1 + 0.2) ** 2 + (value2 + 0.2) ** 2 + (value3 - 0) ** 2
            dist_downleft  = (value1 - 0.2) ** 2 + (value2 - 0.2) ** 2 + (value3 - 0) ** 2
            dist_downright = (value1 - 0.2) ** 2 + (value2 + 0.2) ** 2 + (value3 - 0) ** 2

        params = numpy.matrix([[frame, value0, value1, value2, value3, dist_frontal, dist_left, dist_right, dist_top, dist_bottom, dist_upleft, dist_upright, dist_downleft, dist_downright]])
        parameter = numpy.vstack([parameter, params])


    f.closed



maxv0 = numpy.max(parameter[:,1])
maxv1 = numpy.max(parameter[:,2])
minv1 = numpy.min(parameter[:,2])
maxv2 = numpy.max(parameter[:,3])
maxv3 = numpy.max(parameter[:,4])


#print(maxv0)
#print(maxv1)
#print(minv1)
#print(maxv2)
#print(maxv3)
#
#maxv0 = numpy.where(parameter[:,1] == maxv0)
#maxv1 = numpy.where(parameter[:,2] == maxv1)
#minv1 = numpy.where(parameter[:,2] == minv1)

min_frontal = numpy.min(parameter[:,5])
min_left = numpy.min(parameter[:,6])
min_right = numpy.min(parameter[:,7])
min_top = numpy.min(parameter[:,8])
min_bottom = numpy.min(parameter[:,9])
min_upleft = numpy.min(parameter[:,10])
min_upright = numpy.min(parameter[:,11])
min_downleft = numpy.min(parameter[:,12])
min_downright = numpy.min(parameter[:,13])

min_frontal = numpy.where(parameter[:,5] == min_frontal)
min_left = numpy.where(parameter[:,6] == min_left)
min_right = numpy.where(parameter[:,7] == min_right)
min_top = numpy.where(parameter[:,8] == min_top)
min_bottom = numpy.where(parameter[:,9] == min_bottom)
min_upleft = numpy.where(parameter[:,10] == min_upleft)
min_upright = numpy.where(parameter[:,11] == min_upright)
min_downleft = numpy.where(parameter[:,12] == min_downleft)
min_downright = numpy.where(parameter[:,13] == min_downright)

f_frontal = int(parameter[min_frontal])
f_left = int(parameter[min_left])
f_right = int(parameter[min_right])
f_top = int(parameter[min_top])
f_bottom = int(parameter[min_bottom])
f_upleft = int(parameter[min_upleft])
f_upright = int(parameter[min_upright])
f_downleft = int(parameter[min_downleft])
f_downright = int(parameter[min_downright])

frames = [f_frontal, f_left, f_right, f_top, f_bottom, f_upleft, f_upright, f_downleft, f_downright]

print (f_frontal)
print (f_left)
print (f_right)
print (f_top)
print (f_bottom)
print (f_upleft)
print (f_upright)
print (f_downleft)
print (f_downright)


keyframes = ""
if (not os.path.exists(resultdir)):
    os.mkdir(resultdir)
    print('Make directory: ' + resultdir)

lmfolder = resultdir +"/landmarks/"
if (not os.path.exists(lmfolder)):
    os.mkdir(lmfolder)
    print('Make directory: ' + lmfolder)

frfolder = resultdir +"/frames/"
if (not os.path.exists(frfolder)):
    os.mkdir(frfolder)
    print('Make directory: ' + frfolder)

outfolder = resultdir +"/out/"
if (not os.path.exists(outfolder)):
    os.mkdir(outfolder)
    print('Make directory: ' + outfolder)

for frame in frames:
    if keyframes == "":
        keyframes = str(frame)
    else:
        keyframes = keyframes + "," + str(frame)

    print("Copy: " + videodir + "/annot/%06d.pts" % frame, lmfolder + "/%06d.pts" % frame)
    copyfile(videodir + "/annot/%06d.pts" % frame, lmfolder + "/%06d.pts" % frame)
    copyfile(videodir + "/frames/%06d.png" % frame, frfolder + "/%06d.png" % frame)
    copyfile(videodir + "/out/%06d.png" % frame, outfolder + "/%06d.png" % frame)
    copyfile(videodir + "/out/%06d.isomap.png" % frame, outfolder + "/%06d.isomap.png" % frame)
    copyfile(videodir + "/out/%06d.mtl" % frame, outfolder + "/%06d.mtl" % frame)
    copyfile(videodir + "/out/%06d.obj" % frame, outfolder + "/%06d.obj" % frame)
    copyfile(videodir + "/out/%06d.mtl" % frame, outfolder + "/%06d.mtl" % frame)
    copyfile(videodir + "/out/%06d.pngfitting.log" % frame, outfolder + "/%06d.pngfitting.log" % frame)
    copyfile(videodir + "/out/%06d.rendering.json" % frame, outfolder + "/%06d.rendering.json" % frame)

f = open(resultdir+"/keyframes.txt", 'w')
f.write(keyframes)
f.close()

quit()
