from queues import Queue

class PersonNode:
    def __init__(self, name, adjacent=None):

        if adjacent is None:
            adjacent = set()
        
        assert isinstance(adjacent, set), \
            "adjacent must be a set!"

        self.name = name
        self.adjacent = adjacent

    def __repr__(self):
        return f"<PersonNode: {self.name}>"

class FriendGraph:
    def __init__(self):
        self.nodes = set()

    def __repr__(self):
        return f"<FriendGraph: {[node.name for node in self.nodes]}>"

    def add_person(self, person):
        self.nodes.add(person)

    def set_friends(self, person1, person2):
        person1.adjacent.add(person2)
        person2.adjacent.add(person1)

    def are_connected(self, person1, person2):
        queue = Queue()
        seen = set()
        queue.enqueue(person1)

        while not queue.is_empty():
            current = queue.dequeue()
            seen.add(current)
            print("current:", current)
            print("seen:", seen)
            if current is person2:
                return True
            for adjacent in current.adjacent:
                queue.enqueue(adjacent)
        
        return False


    # def are_connected(self, person1, person2):
    #     """Are two people connected? Breadth-first search."""
    #     possible_nodes = Queue()
    #     seen = set()
    #     possible_nodes.enqueue(person1)
    #     seen.add(person1)

    #     while not possible_nodes.is_empty():
    #         current = possible_nodes.dequeue()
    #         print("checking", current)
    #         if current == person2:
    #             return True
    #         seen.add(current)
    #         for adjacent in current.adjacent:
    #             if adjacent not in seen:
    #                 print("added to queue:", adjacent)
    #                 possible_nodes.enqueue(adjacent)

    #     return False

    def are_connected_rec(self, person1, person2, seen=None):
        # on new recursions, person1 becomes the adjacents
        if not seen:
            seen = set()
        print(f"adding {person1}")
        if person1 == person2:
            return True
        seen.add(person1)
        for person in person1.adjacent:
            if person not in seen:
                if self.are_connected_rec(person, person2, seen):
                    return True
        return False


    ## hackbright lecture version
    # def are_connected(self, person1, person2):
    #     """Are two people connected? Breadth-first search."""

    #     possible_nodes = Queue()
    #     seen = set()
    #     possible_nodes.enqueue(person1)
    #     seen.add(person1)

    #     while not possible_nodes.is_empty():
    #         person = possible_nodes.dequeue()
    #         print("checking", person)
    #         if person is person2:
    #             return True
    #         else:
    #             for friend in person.adjacent - seen:
    #                 possible_nodes.enqueue(friend)
    #                 seen.add(friend)
    #                 print("added to queue:", friend)
    #     return False


nikki = PersonNode("Nikki")
trisha = PersonNode("Trisha")
nescee = PersonNode("Nescee")
cielo = PersonNode("Cielo")
tricia = PersonNode("Tricia")

friends = FriendGraph()
friends.add_person(nikki)
friends.add_person(trisha)
friends.add_person(nescee)
friends.add_person(cielo)
friends.add_person(tricia)
friends.set_friends(nikki, trisha)
friends.set_friends(trisha, nescee)
friends.set_friends(nescee, cielo)


harry = PersonNode("Harry")
hermione = PersonNode("Hermione")
ron = PersonNode("Ron")
neville = PersonNode("Neville")
trevor = PersonNode("Trevor")
fred = PersonNode("Fred")
draco = PersonNode("Draco")
crabbe = PersonNode("Crabbe")
goyle = PersonNode("Goyle")

hogwarts = FriendGraph()
for node in [harry, hermione, ron, neville, fred, draco, crabbe, goyle]:
    hogwarts.add_person(node)

hogwarts.set_friends(harry, hermione)
hogwarts.set_friends(harry, ron)
hogwarts.set_friends(harry, neville)
hogwarts.set_friends(hermione, ron)
hogwarts.set_friends(neville, hermione)
hogwarts.set_friends(neville, trevor)
hogwarts.set_friends(ron, fred)
hogwarts.set_friends(draco, crabbe)
hogwarts.set_friends(draco, goyle)