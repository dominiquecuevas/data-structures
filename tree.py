class Node:
    def __init__(self, data, children):
        self.data = data
        self.children = children

    def __repr__(self):
        return f"<Node data ={self.data}>"

    def find(self, data):
        to_visit = [self]                       # start at node
        while to_visit:                         # loop while there are still nodes
            current = to_visit.pop()            # set current to last item (DFS)
            if current.data == data:
                return current
            to_visit.extend(current.children)   # add to search list

class Tree:
    def __init__(self, root):
        self.root = root

    def __repr__(self):
        return f"<Tree root={self.root}>"

