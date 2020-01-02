class Stack:
    """Define a stack class with the operations
        push
        pop
        peek
        isEmpty
        size

        Chose a built-in python list as data structure for items attribute and the end
        as the top of the stack.
        push is O(1) constant time
        pop is O(1) for removing from the end of a python list
        peek is O(1) for indexing
        isEmpty is O(1) for checking if the list is empty
        size is O(1) since native lists 
        If the beginning of the list was the top of the stack, pop would be O(n) 
        and push would also be O(n) and not the best runtime
    """

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def __repr__(self):
        return f"<Stack items={self.items}>"

def revstring(string):
    """using a stack return a string reversed"""
    s = Stack()
    for letter in string:
        s.push(letter)
    reversedstr = ""
    while not s.isEmpty():
        reversedstr += s.pop()
    return reversedstr

if __name__ == "__main__":
    print(revstring('Nikki'))