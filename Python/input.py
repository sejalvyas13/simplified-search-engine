from search import SearchEngine
 
class Input():
    s = SearchEngine()
    
    def __init__(self):
        with open('inputLinks.txt', 'r') as file :
            links = file.read().replace('\n', '').replace('\r','')
        links = links.split(',')
        self.s.init(links)
    
    def search(self, query):
        file1 = open("output.txt","w+") 
        file1.write(str(self.s.searchString(query)))
        file1.close() 
        return self.s.searchString(query)
 
    
    
#a = Input()
#query = 'hosting'
#print(a.search(query))


