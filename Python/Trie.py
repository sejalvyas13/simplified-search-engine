class TrieNode () :
    isEnd = False
    children = [None]*26
    value = None
    
    def __init__(self):
        self.children = [None]*26
        self.isEnd = False
        self.value = None
        
class Trie () :
    root = None
    def __init__(self) :
        self.root = TrieNode()
        self.root.value = '*'
        
    def insert(self, word) :
        node = self.root
        for i in range(len(word)) :
            if node.children[ord(word[i]) - ord('a')] is None :
                node.children[ord(word[i]) - ord('a')] = TrieNode()
                node.children[ord(word[i]) - ord('a')].value = word[i]
            node = node.children[ord(word[i]) - ord('a')]
        node.isEnd = True
        
        
      
    def search(self,  word) :
        node = self.root
        for i in range(len(word)) :
            if (ord(word[i]) - ord('a')) > 26 or (ord(word[i]) - ord('a')) < 0 :
                return False
            elif not node.children[ord(word[i]) - ord('a')] or node.children[ord(word[i]) - ord('a')].value != word[i] :
                return False
            node = node.children[ord(word[i]) - ord('a')]
        if node.isEnd :
            return True
            
            
           
                
        
        
        
        
    