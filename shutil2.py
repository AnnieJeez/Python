import os
import shutil

path = "C:/Users/user/Downloads/Annie's VS/Python/SourceFolder/"
dpath = "C:/Users/user/Downloads/Annie's VS/Python/DestFolder/"
if(os.path.exists(path)):
    # print("Exists!!!")
    files = os.listdir(path)
    # print(files)
    for file in files:
        splitArray = os.path.splitext(file)
        print(splitArray[1])
        if(splitArray[1]==".jpeg"):
            shutil.move(path+ splitArray[0]+splitArray[1],dpath+ splitArray[0]+splitArray[1])
else:
    print("Not Exists!!!")