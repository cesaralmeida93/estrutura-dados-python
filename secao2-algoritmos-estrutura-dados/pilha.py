class Stack: #pilha
    
    def __init__(self):
        self.stack = []
        self.len_stack = 0

    # inserção(ao final)
    def push(self, e):
        self.stack.append(e)
        self.len_stack += 1


    # remoção(sempre o último)
    def pop(self):
        if not self.empty():
            self.stack.pop(self.len_stack - 1)
            self.len_stack -= 1

    # retorna o elemento do topo
    def top(self):
        if not self.empty():
            return self.stack[-1]

    # verificar se a pilha está vazia
    def empty(self):
        if self.len_stack == 0:
            return True
        return False

    # verificar o tamanho da pilha
    def stack_length(self):
        return self.len_stack

s = Stack()
print(s.empty())
s.push(1)
s.push(2)
s.push(3)
s.pop()
print(s.top())
print(s.stack)
# s.pop()
# print(s.stack)
# print(s.top())
# s.pop()
# print(s.stack_length())
# print(s.stack)
# print(s.top())
# s.pop()
# print(s.stack)
# print(s.top())