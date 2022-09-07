import requests
import os
import json
import sys

def make_pretty(json_object):
    return json_object

def help():
    #returns command options
    help_text = f'''
    Welcome to the SpaceX API help page.
    Add arguments to commands to get data. You can include as many arguments as you want
    here are a list of arguments you can include:
    "help" - will return this same text
    "Launches" - will return data about the latest launches
    '''
    return help_text

def Launches(): 
    url = "https://api.spacexdata.com/v5/launches/latest"
    response =  requests.get(url)
    data = json.loads(response.text)
    return make_pretty(data)
    #TODO: Make data pretty

argument_dict = {
    "help":help(),
    "Launches":Launches(),
}

if len(sys.argv) == 1:
    print(sys.argv[1:])
    print(help())
else:
    for a in sys.argv[1:]:
        try:
            print(argument_dict[str(a)])
        except:
            print("COMMAND NOT FOUND")