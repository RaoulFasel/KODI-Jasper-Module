import re
import json
import requests


WORDS = ["MEDIA", "BACK", "PLAY", "PAUSE", "STOP", "SELECT", "INFO", "UP", "DOWN"]


def doJson(data, profile):

    kodi_ip = profile['kodi']['IP']
    kodi_port = profile['kodi']['PORT']
    kodi_username = profile['kodi']['USER']
    kodi_password = profile['kodi']['PASS']
    try:
        kodi_mac = profile['kodi']['MAC']
    except KeyError:
        kodi_mac = 0
        print("Kodi mac adress was not defined")
    xbmcUrl = "http://"+kodi_username+":"+kodi_password+"@"+kodi_ip+":"+kodi_port+"/jsonrpc?request="
    data_json = json.dumps(data)
    r = requests.post(xbmcUrl, data_json)


def handle(text, mic, profile):

    """
        Responds to user-input to control KODI.
        
        Current supports:
            -Pause / Play
            -Stop
            -Back
            -Up/Down/Left/Right
            -Info
            -Select

        Arguments:
        	text -- user-input, typically transcribed speech
       		mic -- used to interact with the user (for both input and output)
        	profile -- contains information related to the user (e.g., phone number)
    """
    if bool(re.search(r'\b{0}\b'.format("PAUSE"), text, re.IGNORECASE)) or bool(re.search(r'\b{0}\b'.format("PLAY"), text, re.IGNORECASE)):
        data = {'jsonrpc':'2.0','method':'Player.PlayPause','params':{'playerid':1},'id':1}
        doJson(data, profile)
    elif bool(re.search(r'\b{0}\b'.format("STOP"), text, re.IGNORECASE)):
        data = {'jsonrpc':'2.0','method':'Player.Stop','params':{'playerid':1},'id':1}
        doJson(data, profile)
    elif bool(re.search(r'\b{0}\b'.format("BACK"), text, re.IGNORECASE)):
        data = {'jsonrpc':'2.0','method':'Input.Back','id':1}
        doJson(data, profile)
    elif bool(re.search(r'\b{0}\b'.format("SELECT"), text, re.IGNORECASE)):
        data = {'jsonrpc':'2.0','method':'Input.Select','id':1}
        doJson(data, profile)
    elif bool(re.search(r'\b{0}\b'.format("Down"), text, re.IGNORECASE)):
        data = {'jsonrpc':'2.0','method':'Input.Down','id':1}
        doJson(data, profile)
    elif bool(re.search(r'\b{0}\b'.format("UP"), text, re.IGNORECASE)):
        data = {'jsonrpc':'2.0','method':'Input.Up','id':1}
        doJson(data, profile)
    elif bool(re.search(r'\b{0}\b'.format("INFO"), text, re.IGNORECASE)):
        data = {'jsonrpc':'2.0','method':'Input.Info','id':1}
        doJson(data, profile)
    else:

        mic.say("Sorry I'm not aware of that KODI function yet")

def isValid(text):
    """
        Returns True if the text is related to xbmc.

        Arguments:
        	text -- user-input, typically transcribed speech
    """
    
    return bool(re.search(r'\b(media)\b', text, re.IGNORECASE))