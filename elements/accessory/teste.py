# import module
import os
 
# assign size
size = 0
 
# assign folder path
Folderpath = 'C:/Users/Geetansh Sahni/Documents/R'
 
# get size
for path, dirs, files in os.walk(Folderpath):
    for f in files:
        fp = os.path.join(path, f)
        size += os.path.getsize(fp)
 
# display size
print("Folder size: " + str(size))