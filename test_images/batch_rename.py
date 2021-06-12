import glob, re, os

index = 0
path = "D:\\YOLO_Vehicles_Test\\test_images\\"
for filename in glob.glob(path + "imgs_**.jpg" ):
    index+=1
    print(index)
    #print(filename)
    
    #newfilename_removeleftbracket = re.sub(r'\(', '.', filename)
    #newfilename_removerightbracket = re.sub(r'\)', '', newfilename_removeleftbracket)
    newfilename_removedwhitespace = re.sub(" ", ".", filename)
    newfilename_removedjpg = re.sub(".jpg", "", filename)
    os.rename(filename, ("traffic"+str(index)+".jpg"))
    #os.rename(filename, filename+str(index))

