import urllib.request

#x = urllib.request.urlopen('https://www.google.com')
#print(x.read())

from urllib.parse import urlparse
from urllib import request

'''
url = "https://www.google.com/search?q=python+tutorials"
parsed_url = urlparse(url)

print(parsed_url.scheme)   # https
print(parsed_url.netloc)   # www.google.com
print(parsed_url.query)    # q=python+tutorials

--------------------------------------------------------------
url = 'http://pythonprogramming.net'
values = {'s' : "basic", 'submit' : 'search'}

data = urllib.parse.urlencode(values)
data = data.encode('utf-8')  # put data in bytes

req = urllib.request.Request(url, data)
response = urllib.request.urlopen(req)
responseData = response.read()
print(responseData)

'''
'''
try :
    x = urllib.request.urlopen('https://www.google.com/search?q=test')
    print(x.read())
except Exception as e:
    print(str(e))
'''
'''
try:
    url = 'https://www.google.com/search?q=test'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    }

    req = urllib.request.Request(url, headers=headers)
    resp = urllib.request.urlopen(req)
    respData = resp.read().decode('utf-8')

    with open('withHeaders.txt', 'w', encoding='utf-8') as saveFile:
        saveFile.write(respData)

except Exception as e:
    print(str(e))
'''
'''
---------------------------------------------------
post request

url = 'https://httpbin.org/post'

# 1. Define your data
form_data = {
    'username': 'python_coder',
    'action': 'login',
    'version': 3.12
}

# 2 & 3. Encode the data into bytes
# urlencode turns it into: username=python_coder&action=login&version=3.12
encoded_data = urllib.parse.urlencode(form_data).encode('utf-8')

# 4. Create the request object
# Note: Providing the 'data' argument automatically makes this a POST request
req = urllib.request.Request(url, data=encoded_data)

# Add a header so the server knows we're sending form data
req.add_header('Content-Type', 'application/x-www-form-urlencoded')

# 5. Send and read
with urllib.request.urlopen(req) as response:
    result = response.read().decode('utf-8')
    print(result)

'''
'''
--------------------------------------------------------
Sending JSON Data

import json
url = 'https://httpbin.org/post'
data = {'message': 'Hello from urllib!'}

# Convert dictionary to JSON string, then to bytes
json_data = json.dumps(data).encode('utf-8')

req = urllib.request.Request(url, data=json_data)
# CRITICAL: You must tell the server to expect JSON
req.add_header('Content-Type', 'application/json')

with urllib.request.urlopen(req) as response:
    print(response.read().decode('utf-8'))
'''
