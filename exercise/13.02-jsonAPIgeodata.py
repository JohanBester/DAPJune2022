'''
    Write a Python program similar to http://www.py4e.com/code3/geojson.py.
    - Prompt for a location
    - contact a web service
    - retrieve JSON for the web service
    - parse that data
    - retrieve the first place_id from the JSON.
    - A place ID is an identifier that identifies a place on Google Maps.

    Use this API endpoint that has a static subset of the Google Data:
    -------------------------------------------------------------------
        http://py4e-data.dr-chuck.net/json?

    This API uses the same parameter (address) as the Google API.
    This API also has no rate limit so you can test as often as you like.
    If you visit the URL with no parameters, you get "No address..." response.

    To call the API, you need to include
        -   a key= parameter (42)
        -   provide the address that you are requesting as address= parameter
        -   parameters are URL encoded using urllib.parse.urlencode() function
        -   as shown in http://www.py4e.com/code3/geojson.py

    ** Make sure your code is using the API endpoint as shown above **

    Test Data / Sample Execution:
    ------------------------------
    Test to your program with a location of "South Federal University"
    which will have a place_id of "ChIJNeHD4p-540AR2Q0_ZjwmKJ8".
    Example ...
        $ python3 solution.py
        Enter location: South Federal University
        Retrieving http://py4e-data.dr-chuck.net/json?...
        Retrieved 2445 characters
        Place id ChIJNeHD4p-540AR2Q0_ZjwmKJ8

    Actual data:
    --------------
    Run your program to find the place_id for this location:
        University of Michigan
    Make sure to enter the name and case exactly as above
'''

import urllib.request
import urllib.parse
import urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#   Get address for search
address = input("Enter location: ")
if len(address) < 1:
    #   Just enter to activate this default variable
    address = "South Federal University"
elif len(address) >= 1:
    #   Press any character and Enter to activate this default variable
    address = "University of Michigan"

# Build URL for API endpoint call
serviceURL = "http://py4e-data.dr-chuck.net/json?"
api_key = "42"
params = dict()
params["key"] = api_key
params["address"] = address
url = serviceURL + urllib.parse.urlencode(params)

print("Retrieving", url)

jsonData = urllib.request.urlopen(url, context=ctx).read().decode()
print("Retrieved", len(jsonData), "characters")

try:
    info = json.loads(jsonData)

    if not info or "status" not in info or info["status"] != "OK":
        print("==== Failure To Retrieve ====")
        print(json.dumps(jsonData, indent=4))
    else:
        place_id = info["results"][0]["place_id"]
        print("Place id", place_id)

except:
    info = None
    print("Raw JSON return", jsonData)
