from collections import deque

d = deque([3, -9, 14])
d.append(77)
# d.appendleft(100)
d.append(91)
for i in range(len(d)):
    print(d.popleft())
