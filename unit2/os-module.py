import os
os.remove("spider.txt")
os.rename("first-draft.txt", "finished-piece.txt")
os.path.exists("finished-piece.txt")
os.path.getsize("finished-piece.txt")
os.path.getmtime("spider.txt")

import datetime
timestamp = os.path.getmtime("spider.txt")
datetime.datetime.fromtimestamp(timestamp)
datetime.datetime(2020, 1, 6 ,7)
os.path.abspath("spider.txt")