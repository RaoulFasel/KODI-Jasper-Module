import re
import json
import requests

xbmcName = ""
xbmcIp = ""
xbmcPort = ""
xbmcUsername = ""
xbmcPassword = ""

WORDS = [xbmcName, "PLAY", "PAUSE", "STOP"]

def handle(text, mic, profile):
    """
        Responds to user-input to control XBMC.
        
        Current supports:
            -Pause / Play
            -Stop

        Arguments:
        	text -- user-input, typically transcribed speech
       		mic -- used to interact with the user (for both input and output)
        	profile -- contains information related to the user (e.g., phone number)
    """

    if bool(re.search(r'\b{0}\b'.format("PAUSE"), text, re.IGNORECASE)) or bool(re.search(r'\b{0}\b'.format("PLAY"), text, re.IGNORECASE)):
        mic.say("PLAY PAUSE")
        data = {'jsonrpc':'2.0','method':'Player.PlayPause','params':{'playerid':1},'id':1}
        xbmcUrl = "http://"+xbmcUsername+":"+xbmcPassword+"@"+xbmcIp+":"+xbmcPort+"/json?request="
        data_json = json.dumps(data)
        r = requests.post(xbmcUrlTest, data_json)
    elif bool(re.search(r'\b{0}\b'.format("STOP"), text, re.IGNORECASE)):
        mic.say("STOP")
        data = {'jsonrpc':'2.0','method':'Player.Stop','params':{'playerid':1},'id':1}
        data_json = json.dumps(data)
        xbmcUrl = "http://"+xbmcUsername+":"+xbmcPassword+"@"+xbmcIp+":"+xbmcPort+"/json?request="
        r = requests.post(xbmcUrlTest, data_json)
    else:
        mic.say("Sorry, I don't know how to do that yet")

def isValid(text):
    """
        Returns True if the text is related to xbmc.

        Arguments:
        	text -- user-input, typically transcribed speech
    """
    
    return bool(re.search(r'\b{0}\b'.format(xbmcName), text, re.IGNORECASE))