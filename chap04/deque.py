
from collections import deque

dq = deque()

dq.append(1)
dq.appendleft(2)
dq.append(3)
dq.appendleft(3)
dq.remove(3)
print(dq);
dq.rotate(1)
print(dq);