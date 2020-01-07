class Node:
    def __init__(self, data, children):
        self.data = data
        self.children = children

    def __repr__(self):
        return f"<Node data={self.data}>"

    def find(self, data):
        to_visit = [self]                       # start at node
        while to_visit:                         # loop while there are still nodes
            current = to_visit.pop()            # set current to last item (DFS)
            if current.data == data:
                return current
            to_visit.extend(current.children)   # add to search list

    def find_recursively(self, data, to_visit = []):
        if self.data == data:
            print(self)
            return
        to_visit.extend(self.children)
        if not to_visit:
            print("Not found")
            return
        current = to_visit.pop()
        current.find_recursively(data, to_visit)

class Tree:
    def __init__(self, root):
        self.root = root

    def __repr__(self):
        return f"<Tree root={self.root}>"

dumby = Node("Dumbledore", [])
snape = Node("Snape",[])
flitwick = Node("Flitwick", [])
malfoy = Node("Malfoy", [])
mcgonagall = Node("McGonagall", [])
ron = Node("Ron", [])
hermoine = Node("Hermoine", [])
crabbe = Node("Crabbe", [])
dumby.children.append(snape)
dumby.children.append(flitwick)
snape.children.append(malfoy)
malfoy.children.append(crabbe)
dumby.children.append(mcgonagall)
mcgonagall.children.append(ron)
mcgonagall.children.append(hermoine)
tree = Tree(dumby)