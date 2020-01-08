class BinaryNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self):
        return f"<BinaryNode data={self.data}>"

    def find(self, data):
        """
        O(log n)
        every loop reduces the # of options by half
        """
        current = self
        while current:
            print("checking", current.data)
            if current.data == data:
                return current
            elif data < current.data:
                print("go left")
                current = current.left
            elif data > current.data:
                print("go right")
                current = current.right

anakin = BinaryNode("Anakin")
boba = BinaryNode("Boba")
boba.left = anakin
chewbacca = BinaryNode("Chewbacca")
chewbacca.left = boba
dooku = BinaryNode("Dooku")
chewbacca.right = dooku

emperor = BinaryNode("Emperor")

emperor.left = chewbacca

finn = BinaryNode("Finn")
greedo = BinaryNode("Greedo")
emperor.right = greedo
greedo.left = finn
han = BinaryNode("Han")
ig11 = BinaryNode("IG-11")
greedo.right = ig11
jabba = BinaryNode("Jabba")
ig11.left = han
ig11.right = jabba