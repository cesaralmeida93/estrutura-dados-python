class Stack: #pilha
    
    def __init__(self):
        self.stack = []

    # inserção(ao final)
    def push(self, e):
        self.stack.append(e)

    # remoção(sempre o último)
    def pop(self):
        if not self.empty():
            self.stack.pop(len(self.stack) - 1)

    # retorna o elemento do topo
    def top(self):
        if not self.empty():
            return self.stack[-1]

    # verificar se a pilha está vazia
    def empty(self):
        if len(self.stack) == 0:
            return True
        return False

    # verificar o tamanho da pilha
    def stack_length(self):
        return len(self.stack)

s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.stack)
print(s.top())
s.pop()
print(s.stack)
print(s.top())
s.pop()
print(s.stack_length())
print(s.stack)
print(s.top())
s.pop()
print(s.stack)
print(s.top())