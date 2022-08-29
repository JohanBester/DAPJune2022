'''
    Scraping Numbers from HTML using BeautifulSoup
    Write a Python program that will use urllib to 
        read an HTML file from a URL,
        parse the data, 
        extracting numbers,
        count the lines of numbers, and 
        compute the sum of the numbers.
        
    Data Format:
    The file is a table of names and comment counts. 
    Ignore most of the data in the file except for lines like this:

        <tr><td>Modu</td><td><span class="comments">90</span></td></tr>
        <tr><td>Kenzie</td><td><span class="comments">88</span></td></tr>
        <tr><td>Hubert</td><td><span class="comments">87</span></td></tr>
        
    Find all the <span> tags in the file, and 
        pull out the numbers from the tag, and 
        sum the numbers.

    Sample data: 
        http://py4e-data.dr-chuck.net/comments_42.html 
        (Sum=2553)
    Actual data: 
        http://py4e-data.dr-chuck.net/comments_1613405.html
        (Sum ends with 99)
    
    Sample Execution:
    Enter - http://py4e-data.dr-chuck.net/comments_42.html
    Count 50
    Sum 2...
    
'''

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
if len(url) < 1:
    url = "http://py4e-data.dr-chuck.net/comments_1613405.html"
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
numList = list()

# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    # print('TAG:', tag)
    # print('Contents:', tag.contents[0])

    num = int(tag.contents[0])
    if num > 0:
        numList.append(num)

print(len(numList))
print(sum(numList))
