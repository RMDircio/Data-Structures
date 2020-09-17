"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
### Helpful links
# [Queue](https://en.wikipedia.org/wiki/Queue_(abstract_data_type))


'''

STEP 1

'''
class qQueue:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __repr__(self):
        return f"New array is: {self.storage}"
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.storage.insert(0, value)
        self.size += 1

    def dequeue(self):
        if self.size > 0:
            self.size -= 1
            return self.storage.pop(-1)

k = qQueue()
print(len(k))
k.enqueue(2)
print(k)
k.enqueue(4)
print(k)
k.enqueue(8)
print(k)
k.enqueue(9)
print(k)
k.dequeue()
print(k)

'''

STEP 2

'''
import sys
sys.path.append('/home/regina/Documents/Github_Repos/Computer_Science/2.Data_Structures/CSPT13_DataStructures_gp/DataStructuresI/atrem_lecture')
from linked_lists import LinkedList

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __repr__(self):
        return f"New list is: {self.storage}"
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        # enqueue does not mean start/beginning - means ADD
        # only use this because it has the stupid word 'add'
        self.storage.add_to_tail(value)
        self.size += 1
    
    def dequeue(self):
        # dequeue does not mean end/tail - means REMOVE
         if self.size > 0:
            self.size -= 1
            return self.storage.remove_head()

k = Queue()
print(len(k))
k.enqueue(2)
print(k)
k.enqueue(4)
print(k)
k.enqueue(8)
print(k)
k.enqueue(9)
print(k)
k.dequeue()
print(k)

'''
STEP 3

Because we are using such a small dataset, we do not see the speed or efficiency 
issues that come with using a Queue data structure with an array format. In a Queue
structure the arrays take way longer to sort through the data via indexing to get to the
start or end of the list. For Queues, Linked List are more efficient.


'''