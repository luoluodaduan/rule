import os
import requests

def get_adbyby(url):
    res = requests.get(url)
    if res.status_code != 200:
        raise Exception("Connect error")
    return res.text.split("\n")

adbyby_urls = []
adbyby_urls.append("https://raw.githubusercontent.com/easylist/easylistchina/master/easylistchina.txt")
adbyby_urls.append("https://raw.githubusercontent.com/privacy-protection-tools/anti-AD/master/anti-ad-adguard.txt")

if __name__ == "__main__":
    adbyby = set()
    for url in adbyby_urls:
        rules = set(get_adbyby(url))
        adbyby = adbyby.union(rules)
    adbyby = list(adbyby)
    adbyby.sort()
    adbyby_file = open(os.getcwd() + "/dist/adbyby1.txt", mode="w", encoding="utf-8")
    for line in adbyby:
        if not line.startswith(("#", "!", "！", "[")) and len(line) > 0:
            adbyby_file.write("%s\n" % line.replace("\r", ""))
    adbyby_file.close()
