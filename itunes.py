import requests
import sys
import json

if len(sys.argv) != 2:
    sys.exit()
    
response = requests.get("https://itunes.apple.com/search?entity=song&limit=100&term=" + sys.argv[1])

o = response.json()
for result in o["results"]:
    print(result["trackName"])
    
    
#this is a program that requests data from the itunes api and displays it in the terminal.