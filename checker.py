# -*- coding: utf-8 -*-
"""
Created on Sat May 30 03:00:33 2020

@author: ishan.m.jain
"""

import requests
import random
import time
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

f = open("usernames3.txt", "r")
data = f.readlines()



for un in data:
    time.sleep(3 * random.random())
    url = "https://www.tiktok.com/@"+str(un[:3])
    x = requests.get(url, verify = False)
    if x.status_code == 404:
        print("available - " + un[:3]+ " - " + str(x.status_code) +" "+ str(data.index(un)))
        f2 = open("available.txt", "a")
        f2.write(un)
        f2.close()
    else:
        print("skip - " + un[:3]+ " - " + str(x.status_code) +" "+ str(data.index(un)))
    if int(data.index(un))%20 == 0:
        time.sleep(15)


