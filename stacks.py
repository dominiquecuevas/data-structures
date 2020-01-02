class Stack:
    """Define a stack class with the operations
        push
        pop
        peek
        is_empty
        size

        Chose a built-in python list as data structure for items attribute and the end
        as the top of the stack.
        push is O(1) constant time
        pop is O(1) for removing from the end of a python list
        peek is O(1) for indexing
        is_empty is O(1) for checking if the list is empty
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

    def is_empty(self):
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
    while not s.is_empty():
        reversedstr += s.pop()
    return reversedstr

def parens_balanced(string):
    """are parenthese balanced
        use a stack to easily keep track of parentheses
        loop through string
        add a beginning parentheses to stack
        when there is a closing parentheses,
            pop one of the open parentheses in stack
        the stack should be empty if parenthese are balanced
    """
    parens_stack = Stack()

    for char in string:
        if char == "(":
            parens_stack.push(char)
        elif char == ")":
            if parens_stack.is_empty(): # check for matching begin "("
                return False            # fail quick and fall out of loop if failed to match
            else:
                parens_stack.pop()
    return parens_stack.is_empty()      # stack should be empty if balanced

if __name__ == "__main__":
    print("revstring 'Nikki':", revstring('Nikki'))
    print("revstring 'Millenium':", revstring("Millenium"))
    print("balanced? ((4+2)-(2+1)(1-3))/((4-3)-(2+9)",parens_balanced("((4+2)-(2+1)(1-3))/((4-3)-(2+9)"))
    print("balanced? ((4+2)-(2+1)(1-3)))/(4-3)-(2+9)",parens_balanced("((4+2)-(2+1)(1-3)))/(4-3)-(2+9)"))
    print("balanced? ((4+2)-(2+1)(1-3))/(4-3)-(2+9)",parens_balanced("((4+2)-(2+1)(1-3))/(4-3)-(2+9)"))
