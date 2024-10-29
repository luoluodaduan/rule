import os
import re
import time

def get_from_file(path):
    file = open(path, "r", encoding="utf-8")
    content = file.read()
    file.close()
    return content

values = {
    "build_time": time.strftime("%Y-%m-%d %H:%M:%S"),
    "general": get_from_file(os.getcwd() + "/temp/general.txt"),
    "private": get_from_file(os.getcwd() + "/temp/private.txt"),
    "custom": get_from_file(os.getcwd() + "/temp/custom.txt"),
    "tiktok": get_from_file(os.getcwd() + "/temp/tiktok.txt"),
    "telegram": get_from_file(os.getcwd() + "/temp/telegram.txt"),
    "rewrite": get_from_file(os.getcwd() + "/temp/rewrite.txt"),
    "rewriteplus": get_from_file(os.getcwd() + "/temp/rewriteplus.txt"),
}

def gen_file(name):
    template_file = open(os.getcwd() + "/template/" + name + "-template.conf", mode="r", encoding="utf-8")
    template = template_file.read()
    output_file = open(os.getcwd() + "/gen/" + name + ".conf", mode="w", encoding="utf-8")
    marks = re.findall(r"{{(.+)}}", template)
    for mark in marks:
        template = template.replace("{{" + mark + "}}", values[mark])
    output_file.write(template)
    template_file.close()
    output_file.close()

file_names = [
    "black-ad",
    "white-ad-tiktok",
    "white-tiktok",
]

if __name__ == "__main__":
    for name in file_names:
        gen_file(name)
