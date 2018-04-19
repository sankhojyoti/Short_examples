import webbrowser
import random

sites = random.choice(['google.com', 'youtube.com', '9anime.is'])
visit = "http://{}".format(sites)
webbrowser.open(visit)
