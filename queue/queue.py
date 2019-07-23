class Queue:
    def __init__(self):
        self.size = 0
        # what data structure should we
        # use to store queue elements?
        self.storage = []

    def enqueue(self, item):
        return self.storage.append(item)

    def dequeue(self):
        if self.storage:
            return self.storage.pop(0)

    def len(self):
        return len(self.storage)


''' adding and removing to the end using Lists '''
