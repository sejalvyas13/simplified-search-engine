import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

from process import DataProcess
import string
import collections
from Trie import Trie

class SearchEngine():
    data = DataProcess()
    obj = Trie()
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    
    
    def init(self, links):
        #initialises scraping and processing of pages
        self.data.crawl(links)
        alphabets = string.ascii_lowercase
        for word in self.data.dictOccurenceList.keys() :    #append keys of dictOccurenceList in Trie
            count = 0
            for char in word :                              # only append if characters are english alphabets
                if char in alphabets :
                    count = count + 1
            if count == len(word) :
                print("available search words : ", word)
                self.obj.insert(word)
        print("Printing Trie root node: ", self.obj.root.children)
        print("Printing the occurence dictionary : ",self.data.dictOccurenceList)
        
    
    def searchString(self, query):
        count = 0
        searchTerms = []
        pages = []
        for a in query: 
            if (a.isspace()) == True: 
                count = count + 1
        if count > 0 :
            searchTerms = query.split()         #case : multiple words in search query
        else :
            searchTerms = [query]               #case : single word search
        #print(searchTerms)
        for term in searchTerms :
            if self.obj.search(term) :          # if word is found in the Trie, corresponding occurence list from dictOccurenceList is fetched in constant time
                if pages :
                    pages.extend(self.data.dictOccurenceList[term])         
                else :
                    pages = self.data.dictOccurenceList[term]
        if pages :        
            repeatedPages = [item for item, count in collections.Counter(pages).items() if count > 1]  #if pages are repeated, that means we have 
            rankedPages = self.pageRank(repeatedPages)                                                  #some common links which will be ranked better (placed first)
            nonRepeatingPages = list(set(pages) - set(repeatedPages))
            rankedPages.extend(self.pageRank(nonRepeatingPages))
            return rankedPages
        else :
            return ["Search query not found!"]

            
    def pageRank(self, listOfPages):
        values = [0]*len(listOfPages)
        dictRank = dict(zip(listOfPages, values))
        for link in listOfPages :
            url = link
            html = urllib.request.urlopen(url, context=self.ctx).read()
            soup = BeautifulSoup(html, 'html.parser')
            tags = soup('a')
            for tag in tags:
                hyperlink = (tag.get('href', None))
                if hyperlink :
                    if hyperlink[0] == '/' and hyperlink[1] == '/' :
                        hyperlink = hyperlink[2:]
                    for page in listOfPages :
                        if page.find(hyperlink) != -1 :
                            dictRank[page] = dictRank[page] + 1
        #print(dictRank)
        rankedPages = sorted(dictRank, key=dictRank.get, reverse=True)
        return rankedPages
                    
                
    
        

    


        
