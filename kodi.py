import re
import json
import requests

kodi_ip = ""
kodi_port = ""
kodi_username = ""
kodi_password = ""

WORDS = ["MEDIA", "BACK", "PLAY", "PAUSE", "STOP", "SELECT", "info", "UP", "DOWN"]

def doJson(data):
	xbmcUrl = "http://"+kodi_username+":"+kodi_password+"@"+kodi_ip+":"+kodi_port+"/jsonrpc?request="
	data_json = json.dumps(data)
	r = requests.post(xbmcUrl, data_json)

def handle(text, mic, profile):
    """
        Responds to user-input to control XBMC.
        
        Current supports:
            -Pause / Play
            -Stop
            -Back

        Arguments:
        	text -- user-input, typically transcribed speech
       		mic -- used to interact with the user (for both input and output)
        	profile -- contains information related to the user (e.g., phone number)
    """

    if bool(re.search(r'\b{0}\b'.format("PAUSE"), text, re.IGNORECASE)) or bool(re.search(r'\b{0}\b'.format("PLAY"), text, re.IGNORECASE)):
        data = {'jsonrpc':'2.0','method':'Player.PlayPause','params':{'playerid':1},'id':1}
        doJson(data)
    elif bool(re.search(r'\b{0}\b'.format("STOP"), text, re.IGNORECASE)):
        data = {'jsonrpc':'2.0','method':'Player.Stop','params':{'playerid':1},'id':1}
        doJson(data)
    elif bool(re.search(r'\b{0}\b'.format("BACK"), text, re.IGNORECASE)):
        data = {'jsonrpc':'2.0','method':'Input.Back','id':1}
        doJson(data)
    elif bool(re.search(r'\b{0}\b'.format("SELECT"), text, re.IGNORECASE)):
        data = {'jsonrpc':'2.0','method':'Input.Select','id':1}
        doJson(data)
    elif bool(re.search(r'\b{0}\b'.format("Down"), text, re.IGNORECASE)):
        data = {'jsonrpc':'2.0','method':'Input.Down','id':1}
        doJson(data)
    elif bool(re.search(r'\b{0}\b'.format("UP"), text, re.IGNORECASE)):
        data = {'jsonrpc':'2.0','method':'Input.Up','id':1}
        doJson(data)
    elif bool(re.search(r'\b{0}\b'.format("UP"), text, re.IGNORECASE)):
        data = {'jsonrpc':'2.0','method':'Input.Info','id':1}
        doJson(data)
    else:

        mic.say("Sorry I'm not aware of that KODI function yet")

def isValid(text):
    """
        Returns True if the text is related to xbmc.

        Arguments:
        	text -- user-input, typically transcribed speech
    """
    
    return bool(re.search(r'\b(media)\b', text, re.IGNORECASE))