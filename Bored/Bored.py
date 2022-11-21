import requests
import os
import json
import sys

url = "https://www.boredapi.com/api/"

def help():
    #returns command options
    help_text = f'''
    Welcome to the Bored API help page.
    Add arguments to commands to get data. You can include as many arguments as you want
    here are a list of arguments you can include:
    "help" - will return this same text
    "Activity" - return basic activity
    '''
    return help_text

def Activity(): 
    endpoint = "activity/"
    response =  requests.get(url+endpoint, verify=False)
    data = json.loads(response.text)
    return data
    #TODO: add more endpoint options

argument_dict = {
    "help":help(),
    "Activity":Activity(),
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
