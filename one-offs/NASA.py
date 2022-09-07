from re import L
import requests
import os
import json
import sys

API_KEY = os.getenv("NASA_API")

def help():
    #returns command options
    help_text = f'''
    Welcome to the NASA API help page.
    Add arguments to commands to get data. You can include as many arguments as you want
    here are a list of arguments you can include:
    "help" - will return this same text
    "Asteroids" - returns information about asteroids near earth
    '''
    return help_text

def Asteroids(): 
    url = f"https://api.nasa.gov/neo/rest/v1/neo/browse?api_key={API_KEY}"
    response =  requests.get(url)
    data = json.loads(response.text)
    return data
    #TODO: Make data pretty

argument_dict = {
    "help":help(),
    "Asteroids":Asteroids(),
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