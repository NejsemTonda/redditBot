import requests
import json 
'''
Scraping is going to be hard propably sinvce reddit's changes to is API. Might use manual scraping instead
'''

def get_json(url):
    req = requests.get(url)
    real_url = req.history[0].text
    tokens = real_url.split("/")
    reddit = tokens[tokens.index('r')+1]
    reddit_id = tokens[tokens.index('comments')+1]
    

    return requests.get(f"https://www.reddit.com/r/{reddit}/comments/{reddit_id}.json", headers = {'User-agent': 'your bot 0.1'}).json()

def get_QnA(url):
    data = get_json(url)
    
    question = data[0]['data']['children'][0]['data']['title']
    
    responses = []
    for c in data[1]['data']['children']:
        if 'body' in c['data']:
            responses.append(c['data']['body'])

    return [question]+responses
