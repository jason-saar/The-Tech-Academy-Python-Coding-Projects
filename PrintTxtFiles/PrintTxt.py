import os
import time

fDir = os.getcwd()
dirs = os.listdir(fDir)

for file in dirs:
    fName = file
    abPath = os.path.join(fDir, fName)
    if abPath.endswith('.txt'):
        mTime = os.path.getmtime(abPath)
        local_time = time.ctime(mTime)
        print(file, "Last modified:", local_time)


