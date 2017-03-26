from urllib.parse import urlparse, urlencode
import requests
import pprint
#import vk

AUTHORISE_URL = 'https://oauth.vk.com/authorize'
VERSION = '5.62'
APP_ID = '5944949'

auth_data = {
    'client_id': APP_ID,
    'display': 'mobile',
    'response_type': 'token',
    'scope': 'friends,status,video,groups',
    'v': VERSION
}

print('?'.join((AUTHORISE_URL, urlencode(auth_data))))


token_url = 'https://oauth.vk.com/blank.html#access_token=16124c69865ccab515ec419b8188abe3fa2935b49ebec1ba8b2799f43dd67a3b4092359861cc0c430c370&expires_in=86400&user_id=25359024'

params = {
    'access_token': '16124c69865ccab515ec419b8188abe3fa2935b49ebec1ba8b2799f43dd67a3b4092359861cc0c430c370',
    'v': VERSION
}

#params['user_id'] = 'zharinov_dm'
params['fields'] = 'last_name'

response = requests.get('https://api.vk.com/method/friends.get', params)
pprint.pprint(response.json())