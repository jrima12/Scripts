import requests
import os
import json
import sys

#GET AN API KEY FROM NASA AND PASTE IT IN. ITS FUN AND EASY
API_KEY = os.getenv("NASA_API")

def help():
    #returns command options
    help_text = f'''
    Welcome to the NASA API help page.

    useage: python3 NASA.py <argument 1> <argument 2> ... <argument n>

    each argument is a different function that you can run:

    here are a list of arguments you can include:
    help() - will display the help text
    Asteroids() - returns information about asteroids near earth
    '''
    return help_text

def make_pretty(json_object):
    for i in json_object:
        print(i)
    print(json_object['links'])
    # text = f'''
    # number of asteroids = {str(json_object["page"]["total_elements"])}
    # '''

def Asteroids(): 
    url = f"https://api.nasa.gov/neo/rest/v1/neo/browse?api_key={API_KEY}"
    response =  requests.get(url)
    data = response.json()
    return make_pretty(data)
    #TODO: Make data pretty


argument_dict = {
    "help":help,
    "Asteroids":Asteroids
}


if len(sys.argv) == 1:
    print(help())
else:
    for a in sys.argv[1:]:
        try:
            argument_dict[str(a)]()
        except:
            print("COMMAND NOT FOUND")

