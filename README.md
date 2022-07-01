Trie is an efficient information retrieval data structure.
Using Trie, search complexities can be brought to optimal limit (key length).
If we store keys in a binary search tree, a well balanced BST will need time proportional to M * log N, where M is the maximum string length and N is the number of keys in the tree.
Using Trie, we can search the key in O(M) time. However, the penalty is on Trie storage requirements
Implementation as a dictionary:
A modified trie node is used in this implementation. If the node.isEndofWord is True, then it's definition can be accessed.
I have also created my own database of words and definitions and stored them in database.txt
When the program first runs, it imports all the words from database.txt.
I have added insert feature, which not only adds new words and definitions to the trie structure, but also to the database.txt.
So any word which has ever been  inserted into the dictionary, will become part of the database as well.


Note: Insert words in lowercase only and without spaces. The trie implementation has been specifically for lowercase english alphabet characters.
      However, definitions can contain spaces and uppercase characters as well. 
