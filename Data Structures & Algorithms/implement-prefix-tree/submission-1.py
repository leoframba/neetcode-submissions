class PrefixTree:
    class TrieNode:
        def __init__(self, val=None, end=False):
            self.adj = {}
            self.val = val
            self.end = end

    
    def __init__(self):
        self.root = self.TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for i in range(len(word)):
            char = word[i]
            # if it already exist we move to that node
            if char not in node.adj:
                # if it doesnt exist create it
                node.adj[char] = self.TrieNode(char)
            
            node = node.adj[char]
        
        node.end = True
        return

    def search(self, word: str) -> bool:
        node = self.root
        for i in range(len(word)):
            node = node.adj.get(word[i])
            if not node:
                return False
        
        return node.end
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for i in range(len(prefix)):
            node = node.adj.get(prefix[i])
            if not node:
                return False
        
        return True

        
        