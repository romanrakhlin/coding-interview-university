# Сделаем точную копию dict в Питоне.
# В питоне для борьбы с collisions
# используется Open Adressing.
# А именно random probing.
# Мы же будем использовать linear probing.

class HashTable:

	############
	## Нужное ##
	############

	def __init__(self):
		# Установим максимальное количество элементов,
		# сделаем прям как в питоне и поставим 8.
		self.max_size = 8

		# Дальше нам нужна переменная для слежения за реальной длинной,
		# то есть за количеством созданных элементов.
		self.size = 0

		# После создадим сам array который будет represent наш hash table.
		# Поставим всем его жлементам значение None.
		self.table = [None] * self.max_size

	# Метод для вывода длинны hash table.
	# Тут все просто.
	def __len__(self):
		return self.size

	# Метод для вывода hash table.
	# Тут думаю тоже все просто.
	def __str__(self):
		return str(self.table)

	#########################
	## Основной функционал ##
	#########################

	# Метод для создания и добавления нового элемента в hash table.
	# Создадим параметр next_key и изначально он будет None.
	# Мы будем его задавать если нам придется делать linear probong.
	def __setitem__(self, key, value, next_key = None):
		# Изначально увеличиваем актуальную длинну на 1.
		self.size += 1

		# Потом заданный key пропускаем через hash функцию.
		hashed_key = self.hash_function(key)

		# Тут проверка если произошел collision и сдедался linear probing,
		# то мы передали в метод __setitem__ параметр next_key.
		if next_key != None:
			hashed_key = next_key

		# Давайте поймем что же такое collision.
		# Collision - это ситуация, когда вновь вставленный ключ 
		# сопоставляется с уже занятым слотом в хэше.
		# ВАЖНО! Это именно когда keys совпадают!
		# Тк мы реализовывает linear probing, 
		# тут могут быть случаи когда ячейка просто занята,
		# но keys не совпадают.

		# Если ячейка в hash table по индексу созданному с помощью
		# hash_function уже занята, то:
		# print("Inserting " + str(key) + " to " + str(hashed_key))
		# Можете раскоментировать верхнюю строчку и посмотреть как все работает на самом деле.
		if self.table[hashed_key] is not None:
			# Если key текущей ячейки совпадает с новым key, то:
			# (это и есть провекра на collision)
			if self.table[hashed_key][0] == key:
				# Во первых понизим длинну обратно, ведь 
				# новый элемент мы не добавим.
				# Зададим tuple с key и value
				# и после передадим hashed_key и этот tuple 
				# в вспомагательную функцию add_to_hash_table.
				self.size -= 1
				new_tuple = (key, value)
				self.add_to_hash_table(hashed_key, new_tuple)
				return
			# Если ячейка занята какимто key не совпадающим с заданным, то:
			# (наступает черед linear probing)
			# Просто задаем новый key, который будет на 1 больше предыдущего,
			# если же он равен последнему индексу self.table,
			# то возвращаем его на 0 (на самый первый элемент).
			next_key = self.increase_key(hashed_key)
			# Ну и тут вызываем функцию снова для того чтобы next_key прошел проверку.
			self.__setitem__(key, value, next_key)
			return

		# Если же все число и ячейка по заданному key никем не занята,
		# то просто создаем tuple и кладем его в наш hash table.
		new_tuple = (key, value)
		self.add_to_hash_table(hashed_key, new_tuple)

	# Метод по получению нужного value по заданному key.
	def __getitem__(self, key):
		# Пропускаем заданный key через hash_function.
		hashed_key = self.hash_function(key)

		# Если ячейка в hash_table равно None, то:
		if self.table[hashed_key] is None:
			# Вызываем ошибку
			raise KeyError

		# Если в этой ячейка был проделан linear probing,
		# то, понятное дело, элемент сдвинулся вперед.
		# Вообще мы конеяно понимаем что операция по поиску должна
		# работать за O(1), но в случае с linear probing
		# это допустимо ведь будет сделано максимум пару итераций, то близко к 1.
		# К тому же, это случается не всегда поэтому работа за O(1) в большинсвте случаев.
		if self.table[hashed_key][0] != key:
			# Зададим original_key на всякий.
			original_key = hashed_key

			# Пока key, по индексу = hased_key, полученному из заданного key, 
			# в self.table, не совпадает с искомым key:
			while self.table[hashed_key][0] != key:
				# Каждую итерацию увеличивает hashed_key на 1.
				# Как бы идем по нашем self.table вперед по одному элементу.
				hashed_key = self.increase_key(hashed_key)

				# Так же, чтобы не было бесконечного цикла, будем 
				# проверяем равен ли текущий (увеличенный на 1) hashed_key
				# заданному перед циклом original_key.
				# И так же проверим равна ли текущая ячейка None,
				# если это так то мы идем по какому-то неправильному пути.
				# В обоих случаях выведем ошибку.
				if hashed_key == original_key or self.table[hashed_key] is None:
					raise KeyError

		# Если же все окей или поиск hased_key прошел успешно,
		# то возвращаем value из self.table по индексу hased_key.
		return self.table[hashed_key][1]

	def __delitem__(self, key):
		# Пропускаем заданный key через hash_function.
		hashed_key = self.hash_function(key)

		# Если ячейка в hash_table равно None,
		# то такого элемента не существует.
		if self.table[hashed_key] is None:
			# Вызываем ошибку
			raise KeyError

		# Если в этой ячейка был проделан linear probing,
		# то, понятное дело, элемент сдвинулся вперед.
		# Вообще мы конеяно понимаем что операция по удалению должна
		# работать за O(1), но в случае с linear probing
		# это допустимо ведь будет сделано максимум пару итераций, то близко к 1.
		# К тому же, это случается не всегда поэтому работа за O(1) в большинсвте случаев.
		if self.table[hashed_key][0] != key:
			# Зададим original_key на всякий.
			original_key = hashed_key

			# Пока key, по индексу = hased_key, полученному из заданного key, 
			# в self.table, не совпадает с искомым key:
			while self.table[hashed_key][0] != key:
				# Каждую итерацию увеличивает hashed_key на 1.
				# Как бы идем по нашем self.table вперед по одному элементу.
				hashed_key = self.increase_key(hashed_key)

				# Так же, чтобы не было бесконечного цикла, будем 
				# проверяем равен ли текущий (увеличенный на 1) hashed_key
				# заданному перед циклом original_key.
				# И так же проверим равна ли текущая ячейка None,
				# если это так то мы идем по какому-то неправильному пути.
				# В обоих случаях выведем ошибку.
				if hashed_key == original_key or self.table[hashed_key] is None:
					raise KeyError

		# Если же все окей или поиск hased_key прошел успешно,
		# то ставим элемент в self.table по индексу hased_key на None.
		self.table[hashed_key] = None

	#############################
	## Вспомагательные функции ##
	#############################

	# Вспомагательная функция для метода __setitem__.
	def add_to_hash_table(self, hashed_key, new_tuple):
		# Ставим tuple по заданному индексу.
		# Ведь ячейка же свободна.
		self.table[hashed_key] = new_tuple

		# Прям как и в питоне, если занято больше 2/3,
		# то делаем riseze()
		if self.size >= (2 / 3) * self.max_size:
			self.resize()

	# Это по сути и есть наша хэш функция.
	# Делая hash() над какой-то строкой, мы генерируем абсолютно рандомнлое число
	# и для того чтобы хоть как-то поместить его в наш массив нужно чтобы оно было
	# в пределах 0 и self.size. Для этого мы находим остаток от деления на self.size.
	# Плюс остаток от деления помагает нам избежать отрицательного числа.
	def hash_function(self, key):
		return hash(key) % self.max_size

	# Linear probing работает таким образом что 
	# мы каждый раз шагаем на следующий элемент,
	# проверяя свободен ли он. И вот чтобы шагать на следуюищй элемент,
	# на нужно текущий key передвигать на 1 вперед.
	def increase_key(self, key):
		# Чтобы не было ошибки Index out of range мы проверяем
		# является заданный кей последим элементом self.table
		if key == self.max_size - 1:
			# Если является, ставим его на самый первый элемент self.table
			return 0
		# Если не является, двигаем на 1 вперед.
		return key + 1

	# Вспомагательная функция по resize() hash_table
	# в том случае, если заполнено 2/3 self.table
	def resize(self):
		self.max_size *= 2
		self.size = 0
		old_table = self.table
		self.table = [None] * self.max_size
		for tuple in old_table:
			if tuple is not None:
				# Я если честно сам немного невдупляю почему тут
				# мы так пишем, на и пох, думаю когда-нибудь я это пойму.
				self[tuple[0]] = tuple[1]

# Тестиииим !!!!

# Создаем Hash Table
hash_table = HashTable()

# Добавляем элементы
hash_table["asdf"] = "alpha"
hash_table["asdf"] = "bravo"
hash_table["hysortj"] = "charlie"
hash_table["1234asdhfl"] = "dog"
hash_table["asdflkjh"] = "else"
hash_table["5ohslafj"] = "find"

# Удаляем элемент
del hash_table["hysortj"]

# Выводим наш hash_table
print(hash_table)

# Выводим длинну нашего hash_table
print(len(hash_table))

# Выводим полученный по индексу элемент
print(hash_table["5ohslafj"])

