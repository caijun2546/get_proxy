#!/usr/bin/env python
# coding: utf-8

# In[2]:

import sys
reload(sys)
sys.setdefaultencoding('utf8')

import requests
import json
import pickle
from bs4 import BeautifulSoup
import random
import time


# In[4]:


class test_gaoni:
    def __init__(self):
        print("ok")
    def test(self):
        file_name = '/root/ProxyPool/proxy.data'
        with open(file_name,'rb') as load_f:
            proxy = pickle.load(load_f)
        gaoniip=[]
        for i in proxy:
            try:
                ip_url_next = '://'+ str(i)
                proxies = {'http': 'http' + ip_url_next,'https': 'https' + ip_url_next}
                headers = {
                           # "X-Forwarded-Port": i.split(':')[1],"X-Forwarded-For": i.split(':')[0],
                            }
                r = requests.get('https://httpbin.org/ip',headers=headers, proxies=proxies, timeout=3)
                print(r.text)
                print("get it,gaoniip,save!")
                gaoniip.append(i)
            except:
                print("error!!")
		if gaoniip:
			file_name = '/root/ProxyPool/gaoni.data'
            with open(file_name,'wb') as f:
                pickle.dump(gaoniip,f)


# In[11]:


#test_proxy.split(':')[1]


# In[12]:


#proxies


# In[13]:


#r = requests.get('https://httpbin.org/ip',headers=headers, proxies=proxies, timeout=3)


# In[14]:


#print(r.text)


# In[31]:


#gaoniip

