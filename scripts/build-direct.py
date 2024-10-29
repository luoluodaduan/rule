import os
import requests

def get_direct(url):
    res = requests.get(url)
    if res.status_code != 200:
        raise Exception("Connect error")
    return res.text.split("\n")

direct_urls = []
direct_urls.append("https://raw.githubusercontent.com/Loyalsoldier/surge-rules/release/direct.txt")
direct_urls.append("https://raw.githubusercontent.com/luoluodaduan/Rules/main/temp/direct_custom.txt")

if __name__ == "__main__":
    direct = set()
    for url in direct_urls:
        rules = set(get_direct(url))
        direct = direct.union(rules)
    direct = list(direct)
    direct.sort()
    direct_file1 = open(os.getcwd() + "/dist/direct1.txt", mode="w", encoding="utf-8")
    direct_file2 = open(os.getcwd() + "/dist/direct2.txt", mode="w", encoding="utf-8")
    for line in direct:
        if not line.startswith(("#", "!", "！", "[")) and len(line) > 0:
            line = line.replace(" ", "").replace("\t", "").replace("\r", "")
            direct_file1.write("%s\n" % line)
            direct_file2.write("  - '%s'\n" % line)
    direct_file1.close()
    direct_file2.close()
