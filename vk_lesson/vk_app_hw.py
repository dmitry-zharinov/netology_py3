from urllib.parse import urlparse, urlencode
import requests
import networkx as nx
import matplotlib.pyplot as plt


import pprint
#import vk

AUTHORISE_URL = 'https://oauth.vk.com/authorize'
VERSION = '5.62'
APP_ID = '5944949'

G = nx.Graph()

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
    'access_token': '9f9445f905e0df13608d8d4cdd2aa5ac9281c9b5540cbb38aaefc64ffa537a5a4aaedddff371a86b80fa8',
    'v': VERSION
}

params['user_id'] = 196269662
params['fields'] = 'last_name'

my_friends = requests.get('https://api.vk.com/method/friends.get', params)
pprint.pprint(my_friends.json())

overall_friends = []
friend_data = dict()
#overall_friends.append(params['user_id'])

def get_friends_vk(my_friends, overall_friends):
    for friend in my_friends.json()['response']['items']:
        try:
            print('----------------------------------')
            print('Друзья', friend['first_name'], friend['last_name'], friend['id'])
            #добавить друга в список
            friend_data['user_id'] = friend['id']
            #print('1111111111', friend['id'])
            # выбрать друзей для друга
            params['user_id'] = friend['id']
            print(params)
            fr_of_friends = requests.get('https://api.vk.com/method/friends.get', params)
            #pprint.pprint(fr_of_friends.json())
            #for fr in fr_of_friends.json()['response']['items']:
            #    print('fr', fr)
            #    overall_friends.append(fr['id'])
            #    friend_data['items'] = fr
            friend_data['items'] = fr_of_friends.json()['response']['items']
            ##print(friend_data)
            overall_friends.append(friend_data)
        except KeyError:
            continue
        except TypeError:
            continue
    #return overall_friends

############################33

def add_grapth_edges(data):
    graph_list = list()
    #pint(data)
    #data_set = set(data[0]['items'])
    for friend in data:
        print('tttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttt')
        print(friend)
        w = (data['first_name'], data['last_name'], data['id'])
        graph_list.append(w)
    G.add_edges_from(graph_list)



get_friends_vk(my_friends, overall_friends)

print(overall_friends)

add_grapth_edges(overall_friends)

nx.draw_networkx(G)

plt.show()


