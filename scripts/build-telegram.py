import os
import requests

def get_telegram(url):
    res = requests.get(url)
    if res.status_code != 200:
        raise Exception("Connect error")
    return res.text.split("\n")

telegram_urls = []
telegram_urls.append("https://core.telegram.org/resources/cidr.txt")

if __name__ == "__main__":
    telegram = set()
    for url in telegram_urls:
        rules = set(get_telegram(url))
        telegram = telegram.union(rules)
    telegram = list(telegram)
    telegram.sort()
    telegram_file1 = open(os.getcwd() + "/dist/telegram1.txt", mode="w", encoding="utf-8")
    telegram_file2 = open(os.getcwd() + "/dist/telegram2.txt", mode="w", encoding="utf-8")
    for line in telegram:
        if not line.startswith(("#", "!", "！", "[")) and len(line) > 0:
            line = line.replace(" ", "").replace("\t", "").replace("\r", "")
            telegram_file1.write("IP-CIDR,%s,PROXY,no-resolve\n" % line)
            telegram_file2.write("  - '%s'\n" % line)
    telegram_file1.close()
    telegram_file2.close()
