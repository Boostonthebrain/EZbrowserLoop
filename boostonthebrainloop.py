import webbrowser

import time

import random

while True:
    sites = random.choice(['ebay.com', 'google.com', 'wikipedia.com', 'thepiratebay.org', 'craigslist.org'])
    visit = "http://{}".format(sites)
    webbrowser.open(visit)
    seconds = random.randrange(5, 30)