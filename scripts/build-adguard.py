import os
import requests

def get_adguard(url):
    res = requests.get(url)
    if res.status_code != 200:
        raise Exception("Connect error")
    return res.text.split("\n")

adguard_urls = []
adguard_urls.append("https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/filter_15_DnsFilter/filter.txt")
adguard_urls.append("https://raw.githubusercontent.com/curbengh/malware-filter/gh-pages/phishing-filter-agh.txt")
adguard_urls.append("https://raw.githubusercontent.com/curbengh/malware-filter/gh-pages/urlhaus-filter-agh-online.txt")
adguard_urls.append("https://raw.githubusercontent.com/privacy-protection-tools/anti-AD/master/anti-ad-easylist.txt")

if __name__ == "__main__":
    adguard = set()
    for url in adguard_urls:
        rules = set(get_adguard(url))
        adguard = adguard.union(rules)
    adguard = list(adguard)
    adguard.sort()
    adguard_file = open(os.getcwd() + "/dist/adguard1.txt", mode="w", encoding="utf-8")
    for line in adguard:
        if not line.startswith(("#", "!", "！", "[")) and len(line) > 0:
            adguard_file.write("%s\n" % line.replace("\r", ""))
    adguard_file.close()
