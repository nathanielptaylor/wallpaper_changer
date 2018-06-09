import praw
import urllib.request
import random
import time
import os
import sys

url_list = []
reddit = praw.Reddit(client_id = 'NCOlCOLOBEl5rQ' , client_secret = 'NghZywIWqMGjj0CTzlBP889X0XQ', username = 'DJ-Bluntz', password = 'natcatcher', user_agent = 'wallpapergrabber' )

subreddit = reddit.subreddit('wallpaper')


new_wallpapers = subreddit.new(limit = 5)
hot_wallpapers = subreddit.hot(limit = 5)
counter = 1

def downloader(url):
    if url not in url_list:
        url_list.append(url)
        file_name = random.randint(1, 10000)
        full_file_name = str(file_name) + '.jpg'
        urllib.request.urlretrieve(url, '/Users/nattaylor/downloads/wallpapers/' + full_file_name)
        print('successful download')
    elif url in url_list:
        print('Duplicate file')
        time.sleep(2)
        
    


while 'main loop runs forever' == 'main loop runs forever':

    for wallpaper in new_wallpapers:
        
            
            url = wallpaper.url
            
            downloader(url)
            

    for wallpapers in hot_wallpapers:
        url = wallpaper.url
        downloader(url)
    

    input_pause = input('continue? (y/n):   ')
    if input_pause == 'n':
        print('Ok, enjoy your wallpapers')
        sys.exit()
    


