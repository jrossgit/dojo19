import json
import random
from urllib.request import urlopen

import time
import webbrowser

# set the apikey and limit
API_KEY = "7EB6LOKIJ6Y8"  # test value
GIF_LIMIT = 20

# our test search
SEARCH_TERM = "dance"

# get the top 8 GIFs for the search term


def get_dance_gif():
    r = urlopen(f"https://api.tenor.com/v1/search?q={SEARCH_TERM}&key={API_KEY}&limit={GIF_LIMIT}")

    content = r.read().decode()

    results = json.loads(content)['results']

    return random.choice(results)['media'][0]['gif']['url']


def get_dance_data():
    return urlopen(get_dance_gif()).read()


def run():
    webbrowser.open_new_tab('https://www.youtube.com/watch?v=ZPm3FSTbrQ4')
    time.sleep(10)

    url = get_dance_gif()

    while 1:
        webbrowser.open_new_tab(url)
        last_url = url
        while url == last_url:
            url = get_dance_gif()
        time.sleep(3)


if __name__ == '__main__':
    run()
