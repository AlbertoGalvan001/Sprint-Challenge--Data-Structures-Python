class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.length = 0
        self.storage = []
        self.index = 0

    def append(self, item):
        if self.length >= self.capacity:
            self.storage[self.index] = item
            if self.index < self.capacity - 1:
                self.index += 1
            else:
                self.index = 0

        else:
            self.storage.append(item)
            self.length += 1            

    def get(self):
        return self.storage