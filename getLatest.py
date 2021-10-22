import glob
import os

fileList = glob.glob('./files/*')
latestFile = max(fileList, key=os.path.getctime)
print(latestFile)


