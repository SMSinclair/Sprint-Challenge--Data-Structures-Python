class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def append(self, item):
        self.storage[self.current] = item
        if self.current < (self.capacity-1):
            self.current += 1
        else:
            self.current = 0

    def get(self):
        clean_list = [item for item in self.storage if item]
        return clean_list

# buffer = RingBuffer(3)

# print(buffer.get())   # should return []

# buffer.append('a')
# buffer.append('b')
# buffer.append('c')

# print(buffer.get())   # should return ['a', 'b', 'c']

# # 'd' overwrites the oldest value in the ring buffer, which is 'a'
# buffer.append('d')

# print(buffer.get())   # should return ['d', 'b', 'c']

# buffer.append('e')
# buffer.append('f')

# print(buffer.get())   # should return ['d', 'e', 'f']

# buffer_2 = RingBuffer(5)

# for i in range(50):
#     buffer_2.append(i)
#     print(buffer_2.get())