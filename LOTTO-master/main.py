from bs4 import BeautifulSoup
from urllib.request import urlopen
from collections import Counter
import re
import csv
import html5lib
import requests

line_number = 1
ARAWDATA = []
BRAWDATA = []
OFFICIALDATA = {}
NUMBERS = []
TIMES = []
CHANCE = []
zc = 0
headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }
url = "http://www.ycyeah.site/#/win"
req = requests.get(url, headers)
soup = BeautifulSoup(req.content, 'html5lib')
print(soup.prettify())
'''while line_number <= 50:'''
'''COUNTER = 0  # We will need this later
url = urlopen('http://www.ycyeah.site/#/win')
RAW = url.read()  # Reads data into variable'''
'''url.close()'''  # Closes connection
'''PARSED = Soup(RAW, 'html5lib')  # (DATA, Type of Parser)
tables = PARSED.find_all("meta")
print(tables)'''
'''for line in PARSED.findAll('tr', 'Parity','td',{'color': 'rgb(76,175,80)'}):  # Finds all the 'td' tags with align:right
    if '7' or '9' or '1' in str(line):  # Checks if tag has those char
        pRAW = re.findall('rgb(76,175,80)', str(line))  # Gathers only the dates from that text
        for pline in pRAW:
            ARAWDATA.append(pline)  # Stores data in list for mutation later
            print(pline)
line_number += 1'''
