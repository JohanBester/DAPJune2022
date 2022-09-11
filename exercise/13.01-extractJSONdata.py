"""
write a Python program somewhat similar to http://www.py4e.com/code3/json2.py
The program will prompt for a URL, 
read the JSON data from that URL using urllib,
and then parse and extract the comment counts from the JSON data, 
and compute the sum of the numbers in the file

Two files are provided for this assignment;
A sample file and sum for testing, 
and the actual data
Don't save these files; your program should read directly from the URL.

    Sample data:
    -------------
        http://py4e-data.dr-chuck.net/comments_42.json
        (Sum=2553)
        
    Actual data:
    -------------
        http://py4e-data.dr-chuck.net/comments_1613408.json
        (Sum ends with 14)

DATA FORMAT:
-------------
The data consists of a number of names and comment counts in JSON as follows:
{
  comments: [
    {
      name: "Matthias"
      count: 97
    },
    {
      name: "Geomer"
      count: 97
    }
    ...
  ]
}

Sample Execution:
-------------------
$ python3 solution.py
Enter location: http://py4e-data.dr-chuck.net/comments_42.json
Retrieving http://py4e-data.dr-chuck.net/comments_42.json
Retrieved 2733 characters
Count: 50
Sum: 2...

"""
import urllib.request
import urllib.parse
import urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
if len(url) < 1:
    url = "http://py4e-data.dr-chuck.net/comments_1613408.json"
print('Retrieving', url)

jsonData = urllib.request.urlopen(url, context=ctx).read().decode()
print('Retrieved', len(jsonData), 'characters')

try:
    info = json.loads(jsonData)
except:
    info = None

print("Count:", len(info["comments"]))

sum = 0
for item in info["comments"]:
    sum += item['count']

print("Sum:", sum)
