# Создадим класс QueueNode
# Это и будут элемента queue
class QueueNode:
	def __init__(self, data = None, next = None):
		self.data = data
		self.next = next

	def get_data(self):
		return self.data

	def get_next(self):
		return self.next

	def set_data(self, data):
		self.data = data

	def set_next(self, next):
		self.next = next

# Создадим класс Queue
# Это будет наш queue
# У него будет head и tail, что позволит нам 
# добавлять и удалять за O(1)
class Queue:
	def __init__(self):
		self.head = None
		self.tail = None

	# Этот метод проверяет пустой ли queue.
	# Если да, то возвращает True.
	# Если нет, то возвращает False.
	# Он нам очень поможет в следующих методах!
	def empty(self):
		if self.head == None and self.tail == None:
			return True
		else:
			return False

	# Метод для вывода queue
	def __str__(self):
		cur_queue_node = self.head
		output = ""
		while cur_queue_node != None:
			output += str(cur_queue_node.data) + " "
			cur_queue_node = cur_queue_node.get_next()
		return output

	# Добавление в конец
	# Сначала проверяем есть ли вообще элементы
	# Если нету то задаем head и tail
	# Если же есть, то задаем элемент после tail
	# и переставляем tail на заданный элемент
	def enqueue(self, data):
		new_queue_node = QueueNode(data)
		if self.empty():
			self.head = new_queue_node
			self.tail = new_queue_node
			return
		self.tail.set_next(new_queue_node)
		self.tail = new_queue_node

	# Простое удаление из начала
	# Сначала проверяем есть ли вообще элементы
	# Если нету то выводим ошибку
	# Если же есть, двигаем head вперед
	# После этого обязательно делаем проверку
	# на случай если всего 1 элемент и 
	# при его удалении head сдвинется на None
	# А вот tail по прежнему останется на 
	# удаленном элементе
	# Поэтому нам нужно проверять стали ли head None
	# и если это так, то поставить и tail на None
	def dequeue(self):
		if self.empty():
			print("Can't dequeue empty queue")
			return
		self.head = self.head.get_next()
		if self.head == None:
			self.tail = None

# Создаем Queue
queue = Queue()

# Добавляем в queue
queue.enqueue(2)
queue.enqueue(4)
queue.enqueue(8)
queue.enqueue(16)

# Удаление
queue.dequeue()
queue.dequeue()

# Вывод всех элементов
print(queue)

# Все просто охрененно !!!
# Ведь все операции выполняются за O(1) !
# Тут главное не перепутать и сделать именно так как тут.
# А именно побавлять в конце, а удалять из начала.
# Ведь если сделать наоборот, то тогда
# удаление в конце будет занимать O(n) а нам это не нужно.