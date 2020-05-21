#!/usr/bin/env python
# coding: utf-8

# In[10]:


import requests
import json
import pickle
from bs4 import BeautifulSoup

class get_xicidaili:
    def __init__(self):
        print("ok")
    def get_proxy(self):
        headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Cache-Control":"max-age=0",
        "Connection": "keep-alive",
        "Host": "www.xicidaili.com",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "cross-site",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36" ,
        }
        r = requests.get('https://www.xicidaili.com/nn/',headers= headers)
        soup = BeautifulSoup(r.content,"html.parser")
        # print (soup.find_all('tr'))
        ip_prot = []
        for i in soup.find_all('tr'):
            j = i.find_all(class_="country")
            try:
                #print(i.find_all('td')[1].text)
                #print(i.find_all('td')[2].text)
                #print(j[1].text)
                if j[1].text == "高匿":
                    ip_prot.append(i.find_all('td')[1].text+":"+i.find_all('td')[2].text)

            except:
                print("error!!!")
        file_name = '/root/ProxyPool/proxy.data'
        with open(file_name,'wb') as f:
            f.truncate()
            pickle.dump(ip_prot,f)
        #ip_prot





