import os
import requests

def get_tracker(url):
    res = requests.get(url)
    if res.status_code != 200:
        raise Exception("Connect error")
    return res.text.split("\n")

tracker_urls = []
tracker_urls.append("https://cf.trackerslist.com/all.txt")
tracker_urls.append("https://cf.trackerslist.com/best.txt")
tracker_urls.append("https://cf.trackerslist.com/http.txt")

if __name__ == "__main__":
    tracker = set()
    for url in tracker_urls:
        rules = set(get_tracker(url))
        tracker = tracker.union(rules)
    tracker = list(tracker)
    tracker.sort()
    tracker_file = open(os.getcwd() + "/gen/tracker.txt", mode="w", encoding="utf-8")
    for line in tracker:
        if not line.startswith(("#", "!", "！", "[")) and len(line) > 0:
            tracker_file.write("%s\n\n" % line.replace(" ", "").replace("\t", "").replace("\r", ""))
    tracker_file.close()
