# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'https://www.wikipedia.org/'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

for script in soup(["script", "style"]): # remove all javascript and stylesheet code
    script.extract()
    
textContent = soup.get_text()
print('=========================================================================================')
print('text')
textContent = textContent.replace('\n', ' ').replace('\r', '')
textContent = textContent.strip()
textContent = textContent.lower()
print(textContent)
textContent = textContent.split()

stopWords = set(stopwords.words('english'))
print(stopWords)

filteredText = []

for word in textContent :
    if word not in stopWords :
        filteredText.append(word)
        
        

dict = {}
for word in filteredText :
    if word not in dict :
        dict[word] = 1
    else :
        dict[word] = dict[word] + 1
        
print(dict)

# Retrieve all of the anchor tags
tags = soup('a')
#for tag in tags:
    #print(tag.get('href', None))
    
    

