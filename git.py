#!/usr/bin/python3.6

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