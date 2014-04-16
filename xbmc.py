import re

WORDS = ["GLADOS", "PLAY", "PAUSE"]

def handle(text, mic, profile):
    """
        Responds to user-input to control XBMC.

        Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone number)
    """
    

    mic.say(text)


def isValid(text):
    """
        Returns True if the text is related to xbmc.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\bglados\b', text, re.IGNORECASE))