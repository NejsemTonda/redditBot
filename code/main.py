import os
from argparse import ArgumentParser
from tts import synt_voice
from fbScraping import get_reddits
from scraping import get_QnA
from video import create_video


def main(args):
    if args.filter:
        with open("scraped.txt", 'r') as file:
            scraped = file.read().split()
    else:
        scraped = []
    links = get_reddits() # unfiltred links
    links = list(filter(lambda x: x not in scraped, links))   

    #links = ["https://www.reddit.com/r/AskReddit/s/q4tcjAv0hA", "https://www.reddit.com/r/AskReddit/s/JYvp76RmyM"]

    
    qnas = [get_QnA(link) for link in links]
    
    while len(args.names) != 0 and len(args.names) != len(qnas):
        print("there is not enough names for the links, would you like to spice more names for the videos? (-a if auto)")
        name = input("name for {qnas[len(args.names)][0]}: ")
        if name == "-a":
            name = f"{len(os.listdir('../videos')):04}"

        args.names.append(name)

    if len(args.names) == 0:
        c = len(os.listdir('../videos'))
        while len(args.names) < len(qnas):
            args.names.append(f"{c:04}")
            c += 1
    
    for name, qna in zip(name, qnas):
        for i, text in enumerate(qnas):
            synt_voice(text, name+f"-{i}")

        create_video(name)
    
if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-f", "--filter", action="store_false", help="filter out all the already done reddits")
    parser.add_argument("-n", "--name", nargs="*", help="name of the video (number if not specified)")
    args = parser.parse_args()

    main(args)

   
