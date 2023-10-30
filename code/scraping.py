import requests
import json 
'''
Scraping is going to be hard propably sinvce reddit's changes to is API. Might use manual scraping instead
'''

def get_json(url):
    tokens = url.split("/")
    reddit_id = tokens[tokens.index("comments")+1]

    return requests.get(f"https://www.reddit.com/r/AskReddit/comments/{reddit_id}.json", headers = {'User-agent': 'your bot 0.1'}).json()

url = "https://www.reddit.com/r/AskReddit/comments/vb6pge/horny_redditors_how_to_ask_for_nudes_without/"
data = get_json(url)

question = data[0]['data']['children'][0]['data']['title']

for c in data[1]['data']['children']:
    response = c['data']['body']
    print(response)
    print("="*20)


