class Node:

    def __init__(self, data=None):
        '''initialize node with data and next pointer'''
        self.data = data
        self.next = None


class Queue:

    def __init__(self):
        '''initialize queue with head and tail'''
        print("Queue created")
        self.head = None
        self.tail = None

    def enqueue(self, item):
        '''append item to the tail of the queue'''
        if not isinstance(item, Node):
            item = Node(item)
        print(f"Appending {item.data} to the tail of the Queue")
        if self.is_empty():
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def dequeue(self):
        '''remove and return the node at head of the queue'''
        if not self.is_empty():
            print(f"Removing node at head of the Queue")
            curr = self.head
            self.head = self.head.next
            curr.next = None
            return curr.data
        else:
            return "Queue is empty"

    def is_empty(self):
        '''return True if queue is empty, else return false'''
        return self.head == None

    # def len(self):
    #     '''len returns the number of items in the queue'''
    #     self.size

# class Queue:
#     def __init__(self):
#         self.size = 0
#         # what data structure should we
#         # use to store queue elements?
#         self.storage = []

#     def enqueue(self, item):
#         '''enqueue should add an item to the back of the queue'''
#         return self.storage.append(item)

#     def dequeue(self):
#         '''dequeue should remove and return an item from the front of the queue'''
#         if self.storage:
#             return self.storage.pop(0)

#     def len(self):
#         '''len returns the number of items in the queue'''
#         return len(self.storage)


# ''' adding and removing item using Lists '''
