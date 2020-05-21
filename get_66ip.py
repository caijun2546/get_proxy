#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
import json
import pickle
from bs4 import BeautifulSoup


# In[3]:


class get_66ip:
    def _int_(self):
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
        r = requests.get('http://www.66ip.cn/index.html',headers= headers)
        soup = BeautifulSoup(r.content,"html.parser")
        ip_prot = []
        for i in soup.find_all('tr'):
            try:
                #print(i.find_all('td')[3])
                if i.find_all('td')[3].text == "高匿代理":
                     ip_prot.append(i.find_all('td')[0].text+":"+i.find_all('td')[1].text)
            except:
                print("ok")
            #print(i.find_all('td')[1].text)
        
        r = requests.get('http://www.66ip.cn/2.html',headers= headers)
        soup = BeautifulSoup(r.content,"html.parser")
        for i in soup.find_all('tr'):
            try:
                #print(i.find_all('td')[3])
                if i.find_all('td')[3].text == "高匿代理":
                     ip_prot.append(i.find_all('td')[0].text+":"+i.find_all('td')[1].text)
            except:
                print("ok")
            #print(i.find_all('td')[1].text)
            
        r = requests.get('http://www.66ip.cn/3.html',headers= headers)
        soup = BeautifulSoup(r.content,"html.parser")
        for i in soup.find_all('tr'):
            try:
                #print(i.find_all('td')[3])
                if i.find_all('td')[3].text == "高匿代理":
                     ip_prot.append(i.find_all('td')[0].text+":"+i.find_all('td')[1].text)
            except:
                print("ok")
                
        file_name = '/root/ProxyPool/proxy.data'
        with open(file_name,'rb') as f:
            list1 = pickle.load(f)
            #print(list1)

        with open(file_name,'wb') as f:
            list1.append(ip_prot)
            pickle.dump(list1,f)


# In[51]:


#ip_prot


# In[ ]:




