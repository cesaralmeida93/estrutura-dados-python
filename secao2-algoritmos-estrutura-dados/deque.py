class Deque:
    def __init__(self):
        self.len = 0
        self.deque = []

    # verifica se o Deque está vazio
    def empty(self):
        if self.len == 0:
            return True
        return False

    # insere um elemento no início do Deque
    def push_front(self, e):
        self.deque.insert(0, e)
        self.len += 1

    # insere um elemento no fim do Deque
    def push_back(self, e):
        self.deque.insert(self.len, e)
        self.len += 1

    # remove o primeiro valor do Deque
    def pop_front(self):
        if not self.empty():
            self.deque.pop(0)
            self.len -= 1

    # remove o último valor do Deque
    def pop_back(self):
        if not self.empty():
            self.deque.pop(self.len - 1)
            self.len -= 1

    # retorna o primeiro valor do Deque
    def front(self):
        if not self.empty():
            return self.deque[0]
    
    # retorrna o último valor do Deque
    def back(self):
        if not self.empty():
            return self.deque[-1]    

    def show(self):
        for i in self.deque:
            print(i, end=' ')

d = Deque()

# teste de inserção
print(d.empty())
d.push_front(10) # 10
d.push_front(5) # 5 10
d.push_back(20) # 5 10 20
d.push_front(7) # 7 5 10 20
d.push_back(40)# 7 5 10 20 40
print(d.empty())
d.show()
print('\nfront %d' %d.front()) # imprime 7
print('back %d' %d.back()) # imprime 40

# teste de remoção
d.pop_back() # 7 5 10 20
d.pop_back() # 7 5 10
d.pop_back() 
d.show()
print('\nfront %d' %d.front()) # 5
print('back %d' %d.back()) # 10
