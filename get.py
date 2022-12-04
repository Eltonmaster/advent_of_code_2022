import os
import requests
from bs4 import BeautifulSoup
import json
import datetime

def save_conf(conf):
    with open("conf.json", "w") as f:
        json.dump(conf, f, indent=2)

def init():
    if not os.path.exists("conf.json"):
        while True:
            cookie = input("Session Cookie from adventofcode.com: ")
            if cookie != "": break
        conf = {"cookie": cookie}
        save_conf(conf)
    else:
        with open("conf.json", "r") as f:
            conf = json.load(f)
    return conf
        
def folder_check(conf):
    today = str(datetime.date.today().day).zfill(2)
    conf["today"] = today
    save_conf(conf)
    for i in range(1, int(today)+1):
        if not os.path.exists(f"./{str(i).zfill(2)}"):
            os.mkdir(f"./{str(i).zfill(2)}")
            download_challenge(str(i).zfill(2), conf)
        else:
            if not os.path.exists(f"./{today}/challenge.txt"):
                download_challenge(str(i).zfill(2), conf)
        

def download_challenge(today, conf):
    jar = requests.cookies.RequestsCookieJar()
    jar.set("session", conf["cookie"], domain="adventofcode.com", path="/")
    soup = BeautifulSoup(requests.get(f"https://adventofcode.com/2022/day/{int(today)}", cookies=jar).content, "html.parser")
    challenge = soup.find("article").text
    with open(f"./{today}/challenge.txt", "w") as f:
        f.write(challenge)
    with open(f"./{today}/input.txt", "w") as f:
        f.write(requests.get(f"https://adventofcode.com/2022/day/{int(today)}/input", cookies=jar).text)
    with open(f"./{today}/adventofcode.url", mode='w', newline='\r\n') as f:
        f.write(f"[InternetShortcut]\nURL=https://adventofcode.com/2022/day/{int(today)}")
        


conf = init()
folder_check(conf)


