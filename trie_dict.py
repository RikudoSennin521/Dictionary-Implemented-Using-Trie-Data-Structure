# By Rohan Kumar 


import sys, os 

class TrieNode:
      
    # Trie node class
    def __init__(self):
        self.children = [None]*26
  
        # isEndOfWord is True if node represent the end of the word
        self.isEndOfWord = False
        # stores definition of the word, if node is EndofWord
        self.definition = ''

class Trie:
      
    # Trie data structure class
    def __init__(self):
        self.root = TrieNode()
  
  
    def _charToIndex(self,ch):
          
        # private helper function
        # Converts key current character into index
        # use only 'a' through 'z' and lower case
          
        return ord(ch)-97
    
    
    def insert(self,key,definition):
          
        # If not present, inserts key into trie
        # If the key is prefix of trie node, 
        # just marks leaf node
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
  
            # if current character is not present
            if not pCrawl.children[index]:
                pCrawl.children[index] = TrieNode()
            pCrawl = pCrawl.children[index]
  
        # mark last node as leaf
        pCrawl.isEndOfWord = True
        pCrawl.definition = definition 

    def search(self, key):
          
        # Search key in the trie
        # Returns definition if key  is present 
        # in trie, else returns False
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            if not pCrawl.children[index]:
                return False
            pCrawl = pCrawl.children[index]
  
        #return pCrawl.isEndOfWord
        if pCrawl.isEndOfWord:
            return pCrawl.definition
        else:
            return False


def main():
    file = open('database.txt', 'r')
    text = file.read()

    dictarray = [x.split(':') for x in text.splitlines()]
    file.close()
    #print(dictarray)
    t = Trie()
    for x in dictarray:
        #print(x)
        t.insert(x[0],x[1])
    
    flag = 1
    while flag:
        print('------------------------------------------------')
        print('1. Search')
        print('2. Insert')
        print('3. Show entire dictionary')
        print('-1.Exit')
        print('Choose your option:')
        inp = input()
        #inp = 'visualize'
        if inp == '-1':
            flag = 0
        elif inp == '1':
            print('Enter word to search:')
            meaning = t.search(input())
            if meaning is False:
                print('Word not found')
            else:
                print('The definition is:',meaning)
        
        elif inp == '2':
            print('Enter word to insert:')
            word = input()
            print('Enter its definition:')
            defn = input()
            t.insert(word,defn)
            afile = open('database.txt','a')
            if (os.path.getsize('database.txt') > 0):
                afile.write('\n' + word + ':' + defn)
            else:
                afile.write(word + ':' + defn)
            afile.close()


        elif inp == '3':
            for x in dictarray:
                print(x[0])


        
    



main()  
