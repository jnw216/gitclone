#!/usr/bin/python3.6

# this is the command line utility used as a gitclone to interact with gitclone.herokuapp.com
# made by Jonathan N. Winters for Advanced Python class at NYU SPS


import requests, sys

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
    print("adding file")
elif sys.argv[1] == "commit":
    if sys.argv[2] != "-m":
        print("Command Invalid")
    m = sys.argv[3]
    result = m
else:
    result = "Command Invalid"
    

print(result)