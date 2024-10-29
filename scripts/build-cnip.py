import os
import requests

def get_cnip(url):
    res = requests.get(url)
    if res.status_code != 200:
        raise Exception("Connect error")
    return res.text.split("\n")

cnip_urls = []
cnip_urls.append("https://ispip.clang.cn/all_cn.txt")
cnip_urls.append("https://ispip.clang.cn/all_cn_ipv6.txt")

if __name__ == "__main__":
    cnip = set()
    for url in cnip_urls:
        rules = set(get_cnip(url))
        cnip = cnip.union(rules)
    cnip = list(cnip)
    cnip.sort()
    cnip_file1 = open(os.getcwd() + "/dist/cnip1.txt", mode="w", encoding="utf-8")
    cnip_file2 = open(os.getcwd() + "/dist/cnip2.txt", mode="w", encoding="utf-8")
    for line in cnip:
        if not line.startswith(("#", "!", "！", "[")) and len(line) > 0:
            line = line.replace(" ", "").replace("\t", "").replace("\r", "")
            cnip_file1.write("IP-CIDR,%s\n" % line)
            cnip_file2.write("  - '%s'\n" % line)
    cnip_file1.close()
    cnip_file2.close()
