"""
    write a program like https://py4e.com/code3/geoxml.py 
    The program will prompt for a URL, 
    read the XML data from that URL using urllib, and 
    parse and extract the comment counts from the XML data, 
    compute the sum of the numbers in the file and print the sum
    
    We provide two files for this assignment;
    A sample file and sum for testing, and the actual data
    
    Sample data:
    -------------
        http://py4e-data.dr-chuck.net/comments_42.xml 
        (characters=4189, count=50, Sum=2553)
        
    Actual data:
    -------------
        http://py4e-data.dr-chuck.net/comments_1613407.xml
        (Sum ends with 16)
    
    Don't save these files; your program should read directly from the URL.

    Data Format and Approach:
    Data consists of several names and comment counts in XML as follows:
        <comment>
            <name>Matthias</name>
            <count>97</count>
        </comment>
    Look through the <comment> tags to find the <count> values,
    and sum the numbers.
    
    You could use an XPath selector string to look through the XML tree,
    and search for any tag named 'count' with the following line of code:
        counts = tree.findall('.//count')
    See the Python ElementTree documentation and supported XPath syntax for details
    
    You could work from the top of the XML down to the comments node,
    and then loop through the child nodes of the comments node.
    
    Sample Execution:
        $ python3 solution.py
        Enter location: http://py4e-data.dr-chuck.net/comments_42.xml
        Retrieving http://py4e-data.dr-chuck.net/comments_42.xml
        Retrieved 4189 characters
        Count: 50
        Sum: 2...
        
"""

import urllib.request
import urllib.parse
import urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
if len(url) < 1:
    url = "http://py4e-data.dr-chuck.net/comments_1613407.xml"

print('Retrieving', url)
xmlData = urllib.request.urlopen(url, context=ctx).read()
print('Retrieved', len(xmlData), 'characters')

comments = list()
sum = 0

tree = ET.fromstring(xmlData)
comments = tree.findall('comments/comment')
print("Count:", len(comments))

for item in comments:
    comCount = item.find('count').text
    sum += int(comCount)

print("Sum:", sum)
