"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
### Helpful links
# [stack](https://en.wikipedia.org/wiki/Stack_(abstract_data_type))

'''
STEP 1

'''
# can only remove or add from the same side
class aStack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __repr__(self):
        return f"The array is: {self.storage}"
    
    def __len__(self):
        return self.size
    

    # if I add from `end` i can use .append() y .pop()

    # does not mean front it means ADD
    def push(self, value):
        self.storage.append(value)
        self.size += 1

    # does not mean back/end it means REMOVE
    def pop(self):
        if self.size > 0:
            self.size -= 1
            return self.storage.pop()

'''

STEP 2

'''

import sys
sys.path.append('/home/regina/Documents/Github_Repos/Computer_Science/2.Data_Structures/CSPT13_DataStructures_gp/DataStructuresI/atrem_lecture')
from linked_lists import LinkedList

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __repr__(self):
        return f"The new list is: {self.storage}"
    
    def __len__(self):
        return self.size
    
        # if I add from `end` i can use .append() y .pop()

    # does not mean front it means ADD
    def push(self, value):
        self.storage.add_to_head(value)
        self.size += 1

    # does not mean back/end it means REMOVE
    def pop(self):
        if self.size > 0:
            self.size -= 1
            return self.storage.remove_head()

'''

STEP 3

Being that both array and linked lists are really good at knowing where 
the head and tail is, I am not sure if there is any signifcant difference from 
using one or the other.

'''
