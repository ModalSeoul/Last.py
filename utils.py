key = '7d25207fefda375df7db633eae91ef88'

def artist_info(who):
    return ('http://ws.audioscrobbler.com/2.0/?method=artist.getinfo'
            '&artist={}&api_key={}&format=json').format(who, key)
