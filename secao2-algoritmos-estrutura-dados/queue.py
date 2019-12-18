class Queue: # fila

    def __init__(self):
        self.queue = []
        self.len_queue = 0

    # adiciona um novo elemento ao final da fila
    def push(self, e):
        self.queue.append(e)
        self.len_queue += 1

    # remove o primeiro elemento da fila
    def pop(self):
        if not self.empty():
            self.queue.pop(0)
            self.len_queue -= 1

    # Verifica se a fila está vazia
    def empty(self):
        if self.len_queue == 0:
            return True
        return False

    # Verifica o tamanho da fila
    def length(self):
        return self.len_queue

    # Retorna o primeiro elemento da fila
    def front(self):
        if not self.empty():
            return self.queue[0]
        return None

q = Queue()
print(q.empty())
print(q.front())
q.push(1)
q.push(2)
q.push(3)
print(q.empty())
print(q.front())
print(q.queue)
print(q.length())
q.pop()
print(q.queue)
print(q.length())
q.pop()
print(q.queue)
print(q.length())