import requests
import json 
'''
Scraping is going to be hard propably sinvce reddit's changes to is API. Might use manual scraping instead
'''

def get_json(url):
    # this is not working, reddit usses diferent id for sharing and for threads 
    raise NotImplementedError("")
    re
    tokens = url.split("/")
    reddit_id = tokens[-1]
    reddit = tokens[tokens.index('r')+1]

    #request.history
    return requests.get(f"https://www.reddit.com/r/{reddit}/comments/{reddit_id}.json", headers = {'User-agent': 'your bot 0.1'}).json()

def get_QnA(url):
    data = get_json(url)
    print(data)
    
    question = data[0]['data']['children'][0]['data']['title']
    
    responses = []
    for c in data[1]['data']['children']:
        response.append(c['data']['body'])

    return [question]+responses


print(get_QnA("https://www.reddit.com/r/AskReddit/s/q4tcjAv0hA"))
