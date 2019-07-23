class Queue:
    def __init__(self):
        self.size = 0
        # what data structure should we
        # use to store queue elements?
        self.storage = []

    def enqueue(self, item):
        '''enqueue should add an item to the back of the queue'''
        return self.storage.append(item)

    def dequeue(self):
        '''dequeue should remove and return an item from the front of the queue'''
        if self.storage:
            return self.storage.pop(0)

    def len(self):
        '''len returns the number of items in the queue'''
        return len(self.storage)


''' adding and removing item using Lists '''
