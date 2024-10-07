import heapq

class P_queue:
    def __init__(self):
        self.items = []

    def push(self, item):
        heapq.heappush(self.items, -item)

    def empty(self):
        return not self.items
    
    def size(self):
        return len(self.items)

    def pop(self):
        if not self.empty():
            return -heapq.heappop(self.items)

    def top(self):
        if not self.empty():
            return -self.items[0]

count = int(input())
grid = [
    list(map(str, input().split()))
    for _ in range(count)
]
pq = P_queue()

for i in range(count):
    if len(grid[i]) == 2:
        pq.push(int(grid[i][1]))
    elif grid[i][0] == 'pop':
        print(pq.pop())
    elif grid[i][0] == 'size':
        print(pq.size())
    elif grid[i][0] == 'empty':
        temp = pq.empty()
        if temp:
            print(1)
        else:
            print(0)
    elif grid[i][0] == 'top':
        print(pq.top())