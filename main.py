import requests
import json
from time import sleep
from utils import *

"""
This is a script I'm kind of just having fun with.
If it ends up being used a lot, I'll clean it up.
"""

# Aliases
get = requests.get
post = requests.post
patch = requests.patch
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



def get_artists():
    r = get('https://modal.moe/api/artists/')
    return to_json(r.text)

def patch_bio(artist, bio):
    url = 'https://modal.moe/api/artists/{}/name/'.format(artist)
    r = patch(url, data={'bio': bio})
    print(r)

Last = Last()
Artists = get_artists()
for artist in Artists:
    try:
        if len(artist['bio']) > 4:
            bio = Last.artist.info(artist['name'])
            patch_bio(artist['name'], bio)
            sleep(2)
    except Exception as e:
        print(artist)
