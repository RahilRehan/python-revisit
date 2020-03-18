# Using lists as queues

from collections import deque
queue = deque(["Eric", "John", "Michael"])

queue.append("Terry")  #Enqueue
queue.popleft()  #Dequeue

print(queue)