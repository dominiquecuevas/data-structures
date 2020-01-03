class Queue:
    """
    Make a Queue class with the methods
    enqueue(item)
    dequeue()
    is_empty()
    size()
    """

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

people = ["Bill","David","Susan","Jane","Kent","Brad"]
def hot_potato(people, num):
    """
    remove the nth person.

    instantiate a Queue
    enqueue people 
    make a counter when it hits the num
    loop through items and dequeue each
        reset num to 0 if the counter is equal
        if the counter is not at the num, reset counter to zero
    
    """
    queue = Queue()
    for person in people:
        queue.enqueue(person)

    counter = 0
    while queue.size() > 1:
        counter += 1
        dequeued = queue.dequeue()
        if counter == num:
            counter = 0
        else:
            queue.enqueue(dequeued)

        if queue.size() == 1:
            return queue.items[0]


def hotPotato(namelist, num):
    # runestone's answer
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in range(num):        # runeston's answer dequeues after the nth person, num + 1
            simqueue.enqueue(simqueue.dequeue())

        simqueue.dequeue()

    return simqueue.dequeue()

def my_hotPotato(people, num):
    # practice runestone's answer
    queue = Queue()
    for person in people:
        queue.enqueue(person)

    while queue.size() > 1:     # loop while there is more than 1 item
        for n in range(num):    # loop through range upto counter num
            if n + 1 == num:    # add 1 to include in the count to remove
                queue.dequeue() # dequeue to kill off
            else:
                queue.enqueue(queue.dequeue()) # dequeue then enqueue to back of queue

    return queue.items[0] # return the last person left


print("my first attempt:", hot_potato(people, 7))
print("runestone's answer:", hotPotato(people,7))
print("practice runestone with adjustment to count:", my_hotPotato(people, 7))