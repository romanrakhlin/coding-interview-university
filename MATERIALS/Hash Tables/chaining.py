# Пишем стандартный Node класс для LinkedList.
class Node:
	def __init__(self, data = None, next = None):
		self.data = data
		self.next = next

	# Get Methods
	def get_data(self):
		return self.data

	def get_next(self):
		return self.next

	# Set Methods
	def set_data(self, data):
		self.data = data

	def set_next(self, next):
		self.next = next

# Пишем стандартный LinkedList класс.
# Но реализуем только 3 метода.
# Для более полного разбора методов
# смотри туториал по Linked Lists.
class LinkedList:
	def __init__(self):
		self.head = None

	# Добавление в начало.
	def append_front(self, data):
		new_node = Node(data)
		head_node = self.head
		new_node.set_next(head_node)
		self.head = new_node

	# Удаление из начала.
	def remove_front(self):
		head_node = self.head
		self.head = head_node.get_next()

	# Получение первого элемента.
	def get_head(self):
		return self.head.get_data()

# Пишем уже более менее знакомый класс HashTable.
# Знакомый из туториала по Linear Probing.
class HashTable:
	# Та же инициализация.
	def __init__(self):
		self.size = 0
		self.max_size = 8
		self.table = [None] * self.max_size

	# Вывод реализован немного интереснее.
	def __str__(self):
		output = ""

		# Итерируем через все элементы self.table
		for i in self.table:
			# Если элемент не None, то:
			if i != None:
				output += str(i.get_head()[1]) + " "
			# Если None, то так и пишем:
			else:
				output += "None "

		return output

	# Метод добавления элемента в Hash Table.
	def __setitem__(self, key, value):
		# Заданный key пропускаем через hash функцию.
		hashed_key = self.hash_function(key)

		# Зададим тьюпл который хотим положить в hash table.
		new_tuple = (key, value)

		# Если в текущей ячейке еще ничего не было создано, то:
		if self.table[hashed_key] == None:
			# Создаем новый Linked List.
			new_linked_list = LinkedList()
			# Передаем его в self.table по индексу hashed_key.
			self.table[hashed_key] = new_linked_list

		# Берем наш Linked List, лежащий в текущей ячейке.
		cur_linked_list = self.table[hashed_key]
		# И добавляем в head наш тюпл.
		cur_linked_list.append_front(new_tuple)

	# Метод получения value по заданному key.
	def __getitem__(self, key):
		# Заданный key пропускаем через hash функцию.
		hashed_key = self.hash_function(key)

		# Если в текущей ячейке еще ничего не было создано, то:
		if self.table[hashed_key] == None:
			# То выводим ошибку.
			raise KeyError

		# Берем наш Linked List, лежащий в текущей ячейке.
		cur_linked_list = self.table[hashed_key]
		# И возвращаем его голову а именно второй элемент тюпла то есть value.
		return cur_linked_list.get_head()[1]

	# Метод удаления элемента из Hash Table.
	def __delitem__(self, key):
		# Заданный key пропускаем через hash функцию.
		hashed_key = self.hash_function(key)

		# Если в текущей ячейке еще ничего не было создано, то:
		if self.table[hashed_key] == None:
			# То выводим ошибку.
			raise KeyError

		# Берем наш Linked List, лежащий в текущей ячейке.
		cur_linked_list = self.table[hashed_key]
		# И удаляем самый первый элемент (голову).
		cur_linked_list.remove_front()

	# Наша hash функция.
	# Она точно такая же как и в примере реализации linear probing.
	# Могла бы конечно быть более замудренная, то мы не будем особо парится.
	def hash_function(self, key):
		return hash(key) % self.max_size

# Тестиииим !!!!

# Создаем Hash Table
hash_table = HashTable()

# Добавляем элементы
hash_table[1] = 1212
hash_table[2] = 22
hash_table[2] = 44

# Удаляем элемент
del hash_table[2]

# Выводим наш hash_table
print(hash_table)

# Выводим полученный по индексу элемент
print(hash_table[2])

