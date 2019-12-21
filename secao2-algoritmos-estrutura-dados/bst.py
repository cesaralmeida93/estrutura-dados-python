class Node: # Nó

 	def __init__(self, key):
 		self.key = key
 		self.left = None
 		self.right = None

 	# retorna o valor do Nó
 	def getKey(self):
 		return self.key

 	# define o valor do Nó
 	def setKey(self, key):
 		self.key = key

 	# retorna o valor do filho à esquerda
 	def getLeft(self):
 		return self.left

 	# define o valor do filho à esquerda
 	def setLeft(self, left):
 		self.left = left

 	# retorna o valor do filho à direita
 	def getRight(self):
 		return self.right

 	# define o valor o filho à direita
 	def setRight(self, right):
 		self.right = right


class BinarySearchTree:

	def __init__(self):
		self.root = None

	# realiza uma inserção na árvore
	def insert(self, key):

		# cria um novo nó

		node = Node(key)

		# verifica se a árvore está vazia
		if self.empty():
			self.root = node
		else:

			# árvore não vazia, insere recursivamente

			dad_node= None
			curr_node = self.root

			while True:

				if curr_node != None:

					dad_node = curr_node

					# verifica se vai para a esquerda ou direita

					if node.getKey() < curr_node.getKey():
						# vai para a esquerda
						curr_node = curr_node.getLeft()
					else:
						# vai para direita
						curr_node = curr_node.getRight()
				else:

					# se curr_node é None, então encontrou onde inserir

					if node.getKey() < dad_node.getKey():
						dad_node.setLeft(node)
					else:
						dad_node.setRight(node)

					break # sai do loop


	def empty(self):
		if self.root == None:
			return True
		return False

	# mostra em pré-ordem (raiz-esq-dir)
	def show(self, curr_node):

		if curr_node != None:
			print('%d' % curr_node.getKey(), end=' ')
			self.show(curr_node.getLeft())
			self.show(curr_node.getRight())

	def getRoot(self):
		return self.root

n = Node(5)
print(n.getKey())
print(n.getLeft())
print(n.getRight())


t = BinarySearchTree()
t.insert(8)
t.insert(3)
t.insert(1)
t.insert(6)
t.insert(4)
t.insert(7)
t.insert(10)
t.insert(14)
t.insert(13)

t.show(t.getRoot())

