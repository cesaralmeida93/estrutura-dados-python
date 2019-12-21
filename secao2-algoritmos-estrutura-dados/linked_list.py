class Node: # Nó

	def __init__(self, label):
		self.label = label # nome do nó
		self.next = None # referência para o próximo nó

	# Obtém o label
	def getLabel(self):
		return self.label

	# Seta o label
	def setLabel(self, label):
		self.label = label

	# Obtém a referência para o próximo Nó
	def getNext(self):
		return self.next

	# Seta a referência para o próximo Nó
	def setNext(self, next):
		self.next = next


class LinkedList: # Lista Ligada

	def __init__(self):
		self.first = None # Referência para o primeiro nó
		self.last = None # Referência para o último nó
		self.len_list = 0 # Tamanho da lista

	def push(self, label, index): # Insere na lista

		if index >= 0:

			# cria o novo nó
			node = Node(label)

			# verifica se a lista está vazia
			if self.empty():
				self.first = node
				self.last = node
			else:

				if index == 0:
					# inserção no início
					node.setNext(self.first)
					self.first = node
				elif index >= self.len_list:
					# inserção no final
					self.last.setNext(node)
					self.last = node
				else:
					# inserção no meio
					prev_node = self.first
					curr_node = self.first.getNext()
					curr_index = 1

					while curr_node != None:

						if curr_index == index:
							# Seta o curr_node como o próximo do nó
							node.setNext(curr_node)
							# Seta o node como o próximo do prev_node
							prev_node.setNext(node)
							break

						prev_node = curr_node
						curr_node = curr_node.getNext()
						curr_index += 1

			# Atualiza o tamanho da lista
			self.len_list += 1	
	
	# Remoção de elemento
	def pop(self, index):
		if not self.empty() and index >= 0 and index< self.len_list:

			flag_remove = False

			if self.first.getNext() == None:
				# Possui apenas 1 elemento
				self.first = None
				self.last = None
				flag_remove = True
			elif index == 0:
				# Remove do início, mas possui mais de 1 elemento
				self.first = self.first.getNext()
			else:
				'''
					Se chegou aqui é porque a lista possui mais
					de 1 elemento e a remoção não é no início
				'''

				prev_node = self.first
				curr_node = self.first.getNext()
				curr_index = 1

				while curr_node != None:

					if index == curr_index:
						# o próximo do anterior aponta para o próximo do nó corrente
						prev_node.setNext(curr_node.getNext())
						curr_node.setNext(None)
						flag_remove = True
						break

					prev_node = curr_node
					curr_node = curr_node.getNext()
					curr_index += 1

			if flag_remove:
				# atualiza o tamanho da lista
				self.len_list -= 1

	def empty(self):
		if self.first == None:
			return True
		return False

	def length(self):
		return self.len_list

	def show(self):

		curr_node = self.first

		while curr_node != None:
			print(curr_node.getLabel(), end=' ')
			curr_node = curr_node.getNext()
		print('')

lista = LinkedList()

# teste inserção
lista.push('Marcos', 0) # inserção no início
lista.show()
lista.push('Maria', 1) # inserção no final
lista.show()
lista.push('Yankee', 0) # inserção no início
lista.show()
lista.push('Catarina', 2) # inserção no meio
lista.show()
lista.push('Lilica', 4) # inserção no final
lista.show()
lista.push('Sara', 2) # inserção no meio
lista.show()
print('Tamanho da lista: %d\n' % lista.length())

# teste remoção
lista.pop(0) # remoção do início
lista.show()
lista.pop(2) # remoção do meio
lista.show()
lista.pop(3) # remoção do final
lista.show()
print('Tamanho da lista: %d\n' % lista.length())

