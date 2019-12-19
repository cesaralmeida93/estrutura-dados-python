from collections import deque

d = deque()
d.append(1) # adiciona do lado direito do Deque
d.appendleft(2) # adiciona ao lado esquerdo do Deque
d.append(3)
d.appendleft(4)

# 4 2 1 3
d.pop()

# 4 2 1
d.popleft()

# 2 1

for i in d:
    print(i, end=' ')

