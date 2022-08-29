'''
    Write a program that uses urllib to ...
    read the HTML from the data files below,
    extract the href= values from the anchor tags,
    scan for a tag that is in a particular position from the top,
    and follow that link.
    Repeat the process a number of times,
    and report the last name you find.

    We provide two files for this assignment. One is a sample file where we give you the name for your testing and the other is the actual data you need to process for the assignment

    Sample problem:
    ---------------
        Start at http://py4e-data.dr-chuck.net/known_by_Fikret.html
        Find the link at position 3 (the first name is 1).
        Follow that link.
        Repeat this process 4 times.
        The answer is the last name that you retrieve.
        Sequence of names:
            Fikret Montgomery Mhairade Butchi Anayah
        Last name in sequence: Anayah

    Actual problem:
    ---------------
        Start at: http://py4e-data.dr-chuck.net/known_by_Remi.html
        Find the link at position 18 (the first name is 1).
        Follow that link.
        Repeat this process 7 times.
        The answer is the last name that you retrieve.

    Hint:
    The first character of the name of the last page that you'll load is: B

'''

import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL - ')
if len(url) < 1:
    url = "http://py4e-data.dr-chuck.net/known_by_Remi.html"

count = input('Enter count - ')
if len(count) < 1:
    count = 7
iCount = int(count)

position = input('Enter position - ')
if len(position) < 1:
    position = 18
iPosition = int(position)

print(url)

for turns in range(iCount):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    # Retrieve all of the anchor tags
    tags = soup('a')

    for tag in tags:
        if tag == tags[iPosition-1]:
            url = tag.get('href', None)
            print(url)
            exit
        continue
