#!/usr/bin/python3.6

# this is the command line utility used as a gitclone to interact with gitclone.herokuapp.com
# made by Jonathan N. Winters for Advanced Python class at NYU SPS


import requests, sys

#args = argparse.parse_args()


if sys.argv[1] == "pull":
    g = requests.get("http://gitclone.herokuapp.com/pull")
    result = g.text
elif sys.argv[1] == "push":
    g = requests.get("http://gitclone.herokuapp.com/push")
    result = g.text
else:
    result = "Command Invalid"
    

print(result)