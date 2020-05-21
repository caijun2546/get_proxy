#!/usr/bin/env python
# coding: utf-8

import requests
import json
import pickle
import random
import time
from bs4 import BeautifulSoup
from get_xicidaili import get_xicidaili
from get_66ip import get_66ip
from test import test_gaoni


# In[2]:


xicidaili=get_xicidaili()


# In[3]:


xicidaili.get_proxy()


# In[4]:


get66ip = get_66ip()


# In[5]:


get66ip.get_proxy()


# In[6]:


b=test_gaoni()


# In[7]:


b.test()
print("66")

# In[ ]:




