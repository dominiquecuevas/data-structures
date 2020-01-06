class Node:
    def __init__(self, data, children):
        self.data = data
        self.children = children

    def __repr__(self):
        return f"<Node data ={self.data}>"

class Tree:
    def __init__(self, root):
        self.root = root

    def __repr__(self):
        return f"<Tree root={self.root}>"