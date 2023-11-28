# RedditBot - Short videos from reddit scraping
Creating short videos completly automated by python scripts

## What is this doing?

Feel free tu use this code however you want. I use it like this:

1. Step: If reddit page is specified, go to step 2. else:
* open web browser and login to facebook. 
* Scrape all reddit pages from alt. account which I use for sharing reddits 
* Filter already proccessed reddits

2. Step: Scrape reddit pages and get post Head lines and all the comments
3. Step: Synthesise voice from eleven labs api based on the scraped data
4. Create video using MoviePy and with background, music animeted text and so on ...
5. Upload this videos to youtube via youtubes API


### Todo

* tts
    * use eleven labs api ✅
    * create enough of tokens so that I never run out or used cahracters

* reddit scraping
    * get reddit json ✅
    * create question and answers from ask-type reddit ✅
    * create text from all kind of reddit (AITAH, reddit confession, stories, ...)

* generate video
    * generate text video ✅
    * generate background videos ✅
    * add music and sound effects ✅
    * sync voice with text

* API upload to youtube, facebook ...

* scrape the reddit urls from facebook profile ✅
