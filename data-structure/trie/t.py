class Node:
    
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word:str) -> None:
        ptr = self.root

        for letter in word:
            if(letter not in ptr.children):
                ptr.children[letter] = Node()
            ptr = ptr.children[letter]
        ptr.end_of_word = True
        
    def search(self, word:str) -> bool:
        ptr = self.root

        for letter in word:
            if(letter not in ptr.children):
                return False
            ptr = ptr.children[letter]
        
        if(ptr.end_of_word):
            return True
        else:
            return False

    def starts_with(self, prefix: str) -> bool:
        ptr = self.root

        for letter in prefix:
            if(letter not in ptr.children):
                return False
            ptr = ptr.children[letter]

        return True

if __name__ == '__main__':
    obj = Trie()
    obj.insert("word")
    print(obj.search('word'))
    print(obj.starts_with('wor'))
    print(obj.search('world'))
    print(obj.starts_with('worl'))
