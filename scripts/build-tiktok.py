import os
import requests

def get_tiktok(url):
    res = requests.get(url)
    if res.status_code != 200:
        raise Exception("Connect error")
    return res.text.split("\n")

tiktok_urls = []
tiktok_urls.append("https://raw.githubusercontent.com/Semporia/TikTok-Unlock/master/Shadowrocket/TikTok.list")

if __name__ == "__main__":
    tiktok = set()
    for url in tiktok_urls:
        rules = set(get_tiktok(url))
        tiktok = tiktok.union(rules)
    tiktok = list(tiktok)
    tiktok.sort()
    tiktok_file = open(os.getcwd() + "/temp/tiktok.txt", mode="w", encoding="utf-8")
    for line in tiktok:
        if not line.startswith(("#", "!", "！", "[")) and len(line) > 0:
            tiktok_file.write("%s,PROXY\n" % line.replace(" ", "").replace("\t", "").replace("\r", ""))
    tiktok_file.close()
