#!/usr/bin/python3.6

# this is the command line utility used as a gitclone to interact with gitclone.herokuapp.com
# made by Jonathan N. Winters for Advanced Python class at NYU SPS


import requests, sys
import os

#args = argparse.parse_args()

if sys.argv[1] == "pull":
    # generates a list of the latest files
    g = requests.get("http://gitclone.herokuapp.com/pull")
    # for each file in list, pull it using .get to ./[file_name]
    result = g.text
elif sys.argv[1] == "push":
    g = requests.post("http://gitclone.herokuapp.com/push")
    result = g.text
elif sys.argv[1] == "add":
    # if argument is . do all files in current directory
    if sys.argv[2] == ".":
        filelist = os.listdir(os.curdir)
        result = ""
        paths = []      
        for root, dirs, files in os.walk('./'):
            for f in files:
                s = root + f
                if   (    (s.find("/ENV") < 0 ) and s.find("./.git")  < 0  ):
                #if ("./ENV"  not in str(root + f))  ("./.git"  not in str(root + f)):
                    paths.append(root + f)
        for  path in paths:
            result = result + "\nuploading" + path
        
else:
    result = "Command Invalid"
    
print(result)