# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 15:24:52 2020

@author: Gamer
"""

from bs4 import BeautifulSoup

import requests
html = requests.get("http://google.com").text
soup = BeautifulSoup(html, 'html5lib')

first_paragraph = soup.find('p')
first_paragraph_text = soup.p.text
first_paragraph_words = soup.p.text.split()
first_paragraph_id = soup.p['id']
first_paragraph_id2 = soup.p.get('id')