import urllib.request
import random

def downloadWeb(url):
    name = random.randrange(1, 1000)
    full_name = 'Image ' + str(name) + ' .jpg'
    urllib.request.urlretrieve(url, full_name)

print("Enter Image URL: ")
url = input()

downloadWeb(url)

print("Image downloaded successfully...")
