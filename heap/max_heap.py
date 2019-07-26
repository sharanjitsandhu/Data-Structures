class Heap:
    def __init__(self):
        self.storage = []

# insert adds the input value into the heap;
# this method should ensure that the inserted value is in the correct spot in the heap
    def insert(self, value):
        # recieve a piece of value, append it to the end of the heap
        self.storage.append(value)
        # bubble(float) it up to its proper position by calling the _bubble_up function
        # self._bubble_up(len(self.storage)-1)
        return self._bubble_up(self.get_size()-1)

# delete removes and returns the 'topmost' value from the heap;
# this method needs to ensure that the heap property is maintained after the topmost element has been removed.
    # def delete(self):
    #     # 1st possibility: if there are two or more values in the heap
    #     # in that case we want to swap the max value to the very end of the heap before we delete(pop)it off
    #     # and then we want to sift down(float down) the value that we swapped into the top position
    #     # 2nd possibility: if there is only one value in the heap
    #     # in this case we can simply pop the top value off the heap and will have the empty heap after that
    #     # 3rd possibility: if we trying to delete an empty heap
    #     # in which case we just wanna return False
    #     if len(self.storage) > 2:
    #         self.__swap(1, len(self.storage) - 1)
    #         max = self.storage.pop()
    #         self._sift_down(1)
    #     elif len(self.storage) == 2:
    #         max = self.storage.pop()
    #     else:
    #         max = False
    #     return max

    def delete(self):
        if self.storage[0]:
            value = self.storage[0]
            if self.get_size() <= 1:
                self.storage = []
            else:
                self.storage[0] = self.storage.pop(self.get_size()-1)
                self._sift_down(0)
            return value

    # def __swap(self, i, j):
    #     self.storage[i], self.storage[j] = self.storage[j], self.storage[i]

# get_max returns the maximum value in the heap in constant time.
    def get_max(self):
        # checking if we have altleast one value on the heap
        # if we have it return the first value on the heap list
        if self.storage[0]:
            return self.storage[0]
        else:
            # if not simply return False because the heap is empty
            return False

# get_size returns the number of elements stored in the heap.
    def get_size(self):
        return len(self.storage)


# _bubble_up moves the element at the specified index "up" the heap by swapping it with its parent
# if the parent's value is less than the value at the specified index.


    def _bubble_up(self, index):
        # 1st possibility: the index we passed in is the index 0
        # in which case there's no bubbling(floating) to be done
        # it's already at the top

        # will start by finding the parent index of the index we're trying to float
        parent = (index - 1) // 2
        # now we wanna check if the index we passed in is just 0
        if index <= 0:
            return
        elif self.storage[index] > self.storage[parent]:
            self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]
            self._bubble_up(parent)

# _sift_down grabs the indices of this element's children and determines which child has a larger value.
# If the larger child's value is larger than the parent's value,
# the child element is swapped with the parent

    def _sift_down(self, index):
        left = (index * 2) + 1
        right = (index * 2) + 2
        largest = index
        if len(self.storage) > left and self.storage[largest] < self.storage[left]:
            largest = left
        if len(self.storage) > right and self.storage[largest] < self.storage[right]:
            largest = right
        if largest != index:
            self.storage[index], self.storage[largest] = self.storage[largest], self.storage[index]
            self._sift_down(largest)


'''
Max heap is FAST
-->> Insert in O(log n)
-->> Get Max in O(1)
-->> Remove Max in O(log n)
--> Easy to implement using an array
--> eg: if i = 4
        parent(i) = i / 2
        left_child(i) = i * 2
        right_child(i) = i * 2 + 1
'''
