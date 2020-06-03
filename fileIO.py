
import os
import time

fPath = "C:\\1\\a\\"

listDir = os.listdir(fPath)

for file in listDir:
    if ".txt" in file:
        filePath = os.path.join(fPath, file)
        mTime = os.path.getmtime(filePath)
        print('file {} was modified last at {} \n'.format(filePath, mTime)) 
        




