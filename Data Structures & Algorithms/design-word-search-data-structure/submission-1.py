class WordDictionary:

    class TreeNode:
        def __init__(self):
            self.children = {}
            self.end_of_word = False

    def __init__(self):
        self.root = self.TreeNode()
        

    def addWord(self, word: str) -> None:
        current_node = self.root
        for c in word:
            current_node = current_node.children.setdefault(c, self.TreeNode())
        current_node.end_of_word = True
    
        

    def search(self, word: str) -> bool:
        return self.serachHelper(word, self.root)
    
    def serachHelper(self, word: str, node: TreeNode) -> bool:
        if not word: 
            return node.end_of_word
        
        char = word[0]
        if char == ".":
            for child in node.children:
                if self.serachHelper(word[1:], node.children[child]):
                    return True
            return False
        
        if char not in node.children:
            return False
        
        return self.serachHelper(word[1:], node.children[char])
