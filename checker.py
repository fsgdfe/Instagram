# -*- coding: utf-8 -*-
"""
Created on Sat May 30 03:00:43 2020

@author: ishan.m.jain
"""

import requests
import random
import time
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

f = open("usernames3.csv", "r")
data = f.readlines()



for un in data:
    time.sleep(9 * random.random())
    url = "https://www.instagram.com/"+str(un[:9])
    x = requests.get(url, verify = False)
    if x.headers == 'Location':
        print("skip - " + un[:9]+ " - "+ str(data.index(un)))
    else:
        print("available - " + un[:9] + " - "+ str(data.index(un)))
        f2 = open("available.txt", "a")
        f2.write(un)
        f2.close()
    if int(data.index(un))%20 == 0:
        time.sleep(15)


