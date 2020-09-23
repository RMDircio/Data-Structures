# ########## Code from Monday Lecture that is helpful 
# ### noted the functions that can be made inside the delete function

# """
# Each ListNode holds a reference to its previous node
# as well as its next node in the List.
# """
# class ListNode:
#     def __init__(self, value, prev=None, next=None):
#         self.prev = prev
#         self.value = value
#         self.next = next
            
# """
# Our doubly-linked list class. It holds references to 
# the list's head and tail nodes.
# """
# class DoublyLinkedList:
#     def __init__(self, node=None):
#         self.head = node
#         self.tail = node
#         self.length = 1 if node is not None else 0

#     def __len__(self):
#         return self.length
    
#     """
#     Wraps the given value in a ListNode and inserts it 
#     as the new head of the list. Don't forget to handle 
#     the old head node's previous pointer accordingly.
#     """
#     def add_to_head(self, value):
#         # wrap the input value in a node
#         new_node = ListNode(value)
#         # increment the length
#         self.length += 1
#         # check if the linked list is empty
#         if not self.head and not self.tail:
#             # if the list is initially empty, set both head and tail to the new node
#             self.head = new_node
#             self.tail = new_node
#         # we have a non-empty list, add the new node to the head 
#         else:
#             # set the new node's `next` to refer to the current head
#             new_node.next = self.head
#             # set the current head's 'prev' to refer to the new_node (added to make it work with DLL)
#             self.head.prev = new_node
#             # set the list's head reference to the new node 
#             self.head = new_node
        
#     """
#     Removes the List's current head node, making the
#     current head's next node the new head of the List.
#     Returns the value of the removed Node.
#     """
#     def remove_from_head(self):
#         value = self.head.value
#         self.delete(self.head)
#         return value
            
#     """
#     Wraps the given value in a ListNode and inserts it 
#     as the new tail of the list. Don't forget to handle 
#     the old tail node's next pointer accordingly.
#     """
#     def add_to_tail(self, value):
#         new_node = ListNode(value, None, None)
#         self.length += 1
#         if not self.tail and not self.head:
#             self.tail = new_node
#             self.head = new_node
#         else:
#             new_node.prev = self.tail
#             self.tail.next = new_node
#             self.tail = new_node
            
#     """
#     Removes the List's current tail node, making the 
#     current tail's previous node the new tail of the List.
#     Returns the value of the removed Node.
#     """
#     def remove_from_tail(self):
#         value = self.tail.value
#         self.delete(self.tail)
#         return value
            
#     """
#     Removes the input node from its current spot in the 
#     List and inserts it as the new head node of the List.
#     """
#     def move_to_front(self, node):
#         if node is self.head:
#             return
#         value = node.value
#         if node is self.tail:
#             self.remove_from_tail()
#         else:
#             if node.prev:
#                 node.prev.next = node.next
#             if node.next:
#                 node.next.prev = node.prev

#             self.length -= 1
#         self.add_to_head(value)
        
#     """
#     Removes the input node from its current spot in the 
#     List and inserts it as the new tail node of the List.
#     """
#     def move_to_end(self, node):
#         if node is self.tail:
#             return
#         value = node.value
#         if node is self.head:
#             self.remove_from_head()
#         else:
#             if node.prev:
#                 node.prev.next = node.next
#             if node.next:
#                 node.next.prev = node.prev

#             self.length -= 1
#         self.add_to_tail(value)

#     """
#     Deletes the input node from the List, preserving the 
#     order of the other elements of the List.
#     """
#     def delete(self, node):
#         # check of empty list
#         if not self.head and not self.tail:
#             # return nothing
#             return
#         # if list is 1 node long
#         if self.head is self.tail:
#             self.head = None
#             self.tail = None
#         # could make this into a function
#         elif self.head is node:
#             self.head = node.next
#             if node.prev:
#                 node.prev.next = node.next
#             if node.next:
#                 node.next.prev = node.prev
#         # could make this into a function
#         elif self.tail is node:
#             self.tail = node.prev
#             if node.prev:
#                 node.prev.next = node.next
#             if node.next:
#                 node.next.prev = node.prev
#         # could make this into a function        
#         else:
#             if node.prev:
#                 node.prev.next = node.next
#             if node.next:
#                 node.next.prev = node.prev
#         self.length -= 1

#     """
#     Finds and returns the maximum value of all the nodes 
#     in the List.
#     """
#     def get_max(self):
#         if not self.head:
#             return None
#         max_val = self.head.value
#         current = self.head
#         while current:
#             if current.value > max_val:
#                 max_val = current.value
#             current = current.next
#         return max_val



"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def __repr__(self):
        return str(self.value)

    # # code from lecture that might be useful for the assignment
    # ''' 
    # Wrap the given value in a ListNode and insert it after this node. 
    # Note that this node could already have a next node it is pointing to.
    # '''
    # def insert_after(self,value):
    #     current_next = self.next
    #     self.next = ListNode(value, self, current_next)
    #     if current_next:
    #         current_next.prev = self.next

    # '''
    # Wrap the given value in a ListNode and insert it before this node.
    # Note that this node could already have a previous node it is pointing to
    # '''

    # def insert_before(self,value):
    #     current_prev = self.prev
    #     self.prev = ListNode(value, current_prev, self)
    #     if current_prev:
    #         current_prev.next = self.prev

    # '''
    # Rearranges this ListNode's pervious and next pointers accordingly,
    # effectively deleting this ListNode
    # '''

    # def delete(self):
    #     if self.prev:
    #         self.prev.next = self.next
    #     if self.next:
    #         self.next.prev = self.prev




"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList(ListNode):
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def __repr__(self):
        current_node = self.head
        list_string = []
        # while current_node contains a value
        while current_node:
            list_string.append(current_node.value)
            current_node = current_node.next
        return f"The double list: {list_string}"

    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        # make a new node
        new_node = ListNode(value)

        # increase the length by 1
        self.length += 1
        
        # check if the list is empty
        # not in head or in tail
        if not self.head and not self.tail:
            # if list is empty then set node to head and tail
            self.head = new_node
            self.tail = new_node
        
        # if the list contains values - add to head
        else:
            # first make new nodes 'next pointer' --> current head
            new_node.next = self.head
            # make current head 'previous pointer'  --> new node
            self.head.prev = new_node
            # make the new node the head
            self.head = new_node


    def relink_node(self, node: ListNode):
        # if there is a previous node
        if node.prev:
            # make previous node aware of next node
            node.prev.next = node.next
        # if there is a next node    
        if node.next:
            # make next node aware of previous node
            node.next.prev = node.prev

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
         # is the list empty? nothing in head or tail
        if not self.head and not self.tail:
            # return nothing
            return

        # if list is 1 node long - head and tail are the same
        if self.head is self.tail:
            self.head = None
            self.tail = None

        # if node is head - relinked the head
        elif self.head is node:
            self.head = node.next
            self.relink_node(node)

        # if node is tail - relinked the tail
        elif self.tail is node:
            self.tail = node.prev
            self.relink_node(node)

        # relink middle node       
        else:
            self.relink_node(node)
        
        # reset length minus 1     
        self.length -= 1

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        unwanted_node = self.head
        self.delete(unwanted_node)
        return unwanted_node.value 

    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        # make a new node
        new_node = ListNode(value)

        # increase the length by 1
        self.length += 1
        
        # check if the list is empty
        # not in head or in tail
        if not self.head and not self.tail:
            # if list is empty then set node to head and tail
            self.head = new_node
            self.tail = new_node
        
        # if the list contains values - add to tail
        else:
            # first make new nodes 'previous pointer' --> current tail
            new_node.prev = self.tail
            # make current tail 'next pointer'  --> new node
            self.tail.next = new_node
            # make the new node the head
            self.tail = new_node

    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        unwanted_node = self.tail
        self.delete(unwanted_node)
        return unwanted_node.value

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        # resetting the the node
        self.delete(node)
        # take nodes value and place at head
        self.add_to_head(node.value)

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        # resetting the the node
        self.delete(node)
        # take nodes value and place at tail
        self.add_to_tail(node.value)


    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        # check if the list is empty
        # if there is no head
        if not self.head:
            # if list is empty then there's nothing to return
            return None
        
        else:
            # start with the head value
            current_max = self.head.value
            # grab the next value after head to compare
            current_node = self.head.next

            # while current_node contains a value
            while current_node:
                # compare saved max value vs next node
                if current_max < current_node.value:
                    # if max is larger, save that value
                    current_max = current_node.value
                # if max value is NOT larger, move to next node
                current_node = current_node.next
        
        return current_max


# run manual checks
# noob = DoublyLinkedList()
# noob.add_to_head(8)
# noob.add_to_head(4)
# noob.add_to_head(2)
# noob.add_to_head(1)
# print(noob)

# # relink node 2 to 8 ( omit 4)
# print(noob.remove_from_head())
# print(noob)

# # add tail
# noob.add_to_tail('?')
# print(noob)

# # remove tail
# print(noob.remove_from_tail())
# print(noob)

# # move to head
# print('Last')
# print('move to front Q')
# noob.move_to_front(noob.tail)
# print(noob)

# print(noob.delete(noob.head.next))
# print(noob)

# print('move to end Q')
# noob.move_to_end(noob.head)
# print(noob)

# print(noob.get_max())


            
            
        

