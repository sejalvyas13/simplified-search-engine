# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import nltk
from nltk.corpus import stopwords
import string


class DataProcess() :
    dictWordCount = {}
    dictOccurenceList = {}
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    counter = 0
    
    def scrape(self, link):
        # Ignore SSL certificate errors
        url = link
        html = urllib.request.urlopen(url, context=self.ctx).read()
        soup = BeautifulSoup(html, 'html.parser')

        for script in soup(["script", "style"]): # extract function removes all javascript and stylesheet code
            script.extract()
        self.textProcessing(soup.get_text(), url)
        

    def textProcessing(self, rawData, url):
        textContent = rawData
        textContent = textContent.replace('\n', ' ').replace('\r', ' ').replace('.',' ').replace(',',' ').replace(':',' ')
        textContent = textContent.strip()
        textContent = textContent.lower()
        textContent = textContent.split()
        stopWords = set(stopwords.words('english'))
        filteredText = []
        for word in textContent :
            if word not in stopWords :
                filteredText.append(word)
        
        self.indexing(filteredText, url)
            
    def indexing(self, filteredText, url):
        for word in filteredText :
            if word not in self.dictWordCount :
                self.dictWordCount[word] = 1                #dictOccurenceList is a dictionary which stores words and their corresponding links
                self.dictOccurenceList[word] = [url]        #dictOccurenceList is an instance variable which keeps track of the URL in which the word is found
            else :
                self.dictWordCount[word] = self.dictWordCount[word] + 1
                if url not in self.dictOccurenceList[word] : 
                    self.dictOccurenceList[word].append(url)    #dictOccurenceList keeps appending URLs in the corresponding occurence list if a word appeards in more than one URL
                
    def crawl(self, urls):
        for url in urls :
            self.scrape(url)
        #for url in urls : 
        #    html = urllib.request.urlopen(url, context=self.ctx).read()
        #    soup = BeautifulSoup(html, 'html.parser')
        #    tags = soup('a')
        #    for tag in tags:
        #        link = (tag.get('href', None))
        #        if self.counter < 10 and link and 'http' in link :
        #            self.scrape(link)
        #            print(link)
        #            self.counter = self.counter + 1

                
    



    
