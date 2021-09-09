# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 16:36:26 2020

@author: Gamer
"""

import requests, json

endpoint = "https://api.github.com/users/joelgrus/repos"

repos = json.loads(requests.get(endpoint).text)