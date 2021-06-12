import glob, re, os
import cv2

#width = 680 
#height = 480
width = 1680
height = 1050
dim = (width, height)

path = "D:\\YOLO_Vehicles_Test\\test_images\\"
for filename in glob.glob(path + 'traffic**.jpg'):
    newfilename_removedjpg = re.sub(".jpg", "", filename)
    oriimg = cv2.imread(filename, cv2.IMREAD_UNCHANGED)
    resized = cv2.resize(oriimg, dim, interpolation = cv2.INTER_AREA)
    cv2.imwrite(newfilename_removedjpg+"resized16801050.jpg", resized) 
  

