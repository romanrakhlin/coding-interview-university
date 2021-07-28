import collections

collections_queue = collections.deque()

# Добавление
collections_queue.appendleft(2)
collections_queue.appendleft(4)
collections_queue.appendleft(8)
collections_queue.appendleft(16)

# Удаление
collections_queue.pop()
collections_queue.pop()

# Можем даже поиграться создав класс
# Буфер является частью памяти для временного хранения данных
# enqueue - вствать в очередь
# dequeue - выйти из очереди
class Queue:
	def __init__(self):
		self.buffer = collections.deque()

	def enqueue(self, data):
		self.buffer.appendleft(data)

	def dequeue(self):
		self.buffer.pop()

	def is_empty(self):
		return len(self.buffer) == 0

	def size(self):
		return len(self.buffer)

made_with_class = Queue()

# Добавление
made_with_class.enqueue(2)
made_with_class.enqueue(4)
made_with_class.enqueue(8)
made_with_class.enqueue(16)

# Удаление
made_with_class.dequeue()
made_with_class.dequeue()

print(made_with_class)
