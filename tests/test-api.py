# Run test API
import requests
import http
# import sys

PORT = '5022'


# Upload an unsupported file
print("Upload unsupported file")
url = 'http://0.0.0.0:'+PORT+'/v1/models'  # API endpoint
filename = 'test.png'
file = open(filename, 'rb')  # File to upload
try:
    r = requests.post(url=url, files={'file': file})
except requests.exceptions.RequestException as e:  # This is the correct syntax
    print(e)
print(r.status_code)
print(r.text)


# Upload a supported file
print("Upload supported file")
url = 'http://0.0.0.0:'+PORT+'/v1/models'  # API endpoint
filename = 'test.fbx'
file = open(filename, 'rb')  # File to upload
try:
    r = requests.post(url=url, files={'file': file})
except requests.exceptions.RequestException as e:  # This is the correct syntax
    print(e)
print(r.status_code)
print(r.text)


# Upload a supported file by sending the url
print("Post source_path to supported file")
url = 'http://0.0.0.0:'+PORT+'/v1/models'  # API endpoint
source_path = 'https://purplepill.io/wp-includes/3d/test.fbx'
try:
    r = requests.post(url=url, data={'source_path': source_path})
except http.client.HTTPException as e:
    print(e)
except requests.exceptions.RequestException as e:  # This is the correct syntax
    print(e)
print(r.status_code)
print(r.text)


# Upload a supported file by sending the url + arguments for converter
print("Post source_path to supported file + arguments")
url = 'http://0.0.0.0:'+PORT+'/v1/models'  # API endpoint
source_path = 'https://purplepill.io/wp-includes/3d/test.fbx'
try:
    r = requests.post(url=url, data={'source_path': source_path, 'compress': 'true', 'binary': 'true'})
except http.client.HTTPException as e:
    print(e)
except requests.exceptions.RequestException as e:  # This is the correct syntax
    print(e)
print(r.status_code)
print(r.text)
data = r.json()
model_id = data['model_id']


# Upload a file that is too large
print("Upload a file that is too large")
url = 'http://0.0.0.0:'+PORT+'/v1/models'  # API endpoint
source_path = 'https://purplepill.io/wp-includes/3d/large.zip'
try:
    r = requests.post(url=url, data={'source_path': source_path})
except http.client.HTTPException as e:
    print(e)
except requests.exceptions.RequestException as e:  # This is the correct syntax
    print(e)
print(r.status_code)
print(r.text)


# Get list of all models
print("Get list of all models")
url = 'http://0.0.0.0:'+PORT+'/v1/models'  # API endpoint
try:
    r = requests.get(url=url)
except requests.exceptions.RequestException as e:  # This is the correct syntax
    print(e)
print(r.status_code)
print(r.text)


# Get non-existing model
print("Get non-existing model")
url = 'http://0.0.0.0:'+PORT+'/v1/models/fakeid99'  # API endpoint
try:
    r = requests.get(url=url)
except requests.exceptions.RequestException as e:  # This is the correct syntax
    print(e)
print(r.status_code)
print(r.text)


# Delete non-existing model
print("Delete non-existing model")
url = 'http://0.0.0.0:'+PORT+'/v1/models/fakeid99'  # API endpoint
try:
    r = requests.delete(url=url)
except requests.exceptions.RequestException as e:  # This is the correct syntax
    print(e)
print(r.status_code)
print(r.text)


# Delete existing model
print("Delete existing model with id %s" % model_id)
url = 'http://0.0.0.0:'+PORT+'/v1/models/' + model_id  # API endpoint
try:
    r = requests.delete(url=url)
except requests.exceptions.RequestException as e:  # This is the correct syntax
    print(e)
print(r.status_code)
print(r.text)


# Delete all models older than x hours
print("Delete all models older than x hours")
url = 'http://0.0.0.0:'+PORT+'/v1/models'  # API endpoint
hours_old = 5
try:
    r = requests.delete(url=url, data={'hours_old': hours_old})
except requests.exceptions.RequestException as e:  # This is the correct syntax
    print(e)
print(r.status_code)
print(r.text)