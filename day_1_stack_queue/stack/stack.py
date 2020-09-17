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
[stack](https://en.wikipedia.org/wiki/Stack_(abstract_data_type))

# can only remove or add from the same side
class Stack:
    def __init__(self):
        self.size = 0
        # self.storage = ?

    def __len__(self):
        pass
    

        # if I add from `end` i can use .append() y .pop()

    # does not mean front it means ADD
    def push(self, value):
        pass
    # does not mean back/end it means REMOVE
    def pop(self):
        pass
