class PrefixTree:

    class Tree_Node:
        def __init__(self, end_of_word):
            self.children = {}
            self.end_of_word = end_of_word
        
        def __str__(self):
            return f"{self.children}, EOW={self.end_of_word}"

             
    
    def __init__(self):
        self.root = self.Tree_Node(False)
        
    # iterate through word adding each char as a node
    def insert(self, word: str) -> None:
        current_node = self.root
        for i, c in enumerate(word):
            next_node = current_node.children.get(c)
            # if the node doesnt exist create it
            if not next_node:
                new_node = self.Tree_Node(False)
                current_node.children[c] = new_node
                next_node = new_node
            current_node = next_node
        current_node.end_of_word = True
                


    def search(self, word: str) -> bool:
        current_node = self.root
        for c in word:
            if c not in current_node.children:
                return False
            current_node = current_node.children[c]
        return current_node.end_of_word
        


    def startsWith(self, prefix: str) -> bool:
        current_node = self.root
        for c in prefix:
            if c not in current_node.children:
                return False
            current_node = current_node.children[c]
        return True