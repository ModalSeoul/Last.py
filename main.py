import requests
import json
from utils import *

"""
This is a script I'm kind of just having fun with.
If it ends up being used a lot, I'll clean it up.
"""

# Aliases
get = requests.get
post = requests.post
to_json = json.loads


class Last:

    def __init__(self):
        self.set_artist() 
    
    class Artist:

        def info(self, name):
            r = get(artist_info(name))
            summ = to_json(r.text)['artist']['bio']['summary']
            return summ.split('<a href="')[0]

    def set_artist(self):
        self.artist = self.Artist()
        
Last = Last()
print(Last.artist.info('Megadeth'))

