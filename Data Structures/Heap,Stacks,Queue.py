from collections import deque
from heapq import heappush, heappop



# Stack
stack=deque()
stack.append(1)
stack.append(2)
stack.append(3)
print(stack.pop()) # 3
print(stack.pop()) # 2

# Queue
queue=deque()
queue.append(1)
queue.append(2)
queue.append(3)
print(queue.popleft()) # 1
print(queue.popleft()) # 2

# Heap
heap=[]
heappush(heap, 3)
heappush(heap, 1)
heappush(heap, 2)
print(heappop(heap)) # 1
print(heappop(heap)) # 2


