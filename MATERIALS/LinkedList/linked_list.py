from node import Node

class LinkedList(object):
	# Зададим head равным None,
	# ведь если обьект ни на что не ссылается,
	# питон удаляет его при компиляции 
	def __init__(self):
		self.head = None

	# __str__() - returns all elements in linked list
	# Можно будет юзать print(наш linked list)
	# Тут мы задаем current_node, он самый первый,
	# то есть head. Задаем еще переменную output для вывода.
	# Проверяем пока current_node хоть чему-то равен,
	# мы добавялем что-то в output и задаем в current_node
	# следующий node. И когда текущий node уже станет None
	# то есть его вообще не будет существовать, то цикл остановится и мы
	# выведем output. Так же если в нашем linked листе вообще
	# нет ни одного элемента, то тоже выведется пустой output
	# ведь при инициализации head по дефолту равен None.
	# Тут подход вообще свой. В отличае от того как это реализовано в append()
	# наша цель это не пройти дойти до того элемента, после
	# которого ничего нет (последнего), а сохранить все итерации
	# и проитерировать именно столько раз, сколько всего элементов в
	# linked listе и записать их все.
	def __str__(self):
		current_node = self.head
		output = ""
		while current_node != None:
			output += str(current_node.data) + " -> "
			current_node = current_node.get_next()
		return output

	# __len__() - returns number of data elements in list
	# Тут будет все то же самое что и в предыдущем методе.
	# Так же будем задавать current_node и проделать
	# итерации с проверкам. Но в этот раз вместо добавления
	# инфы в output, мы будем увеличивать count и выведем его в конце.
	def __len__(self):
		count = 0
		current_node = self.head
		while current_node != None:
			count += 1
			current_node = current_node.get_next()
		return count

	# append(value) - adds an item at the end
	# Данный метод принимает data и мы создаем переменную
	# new_node который наследуется от класса Node. 
	# После этого идет проверка на то что еще не создано
	# ни одного элемента и если это так то мы задаем head.
	# Важно что при создании мы задаем только data, а вот next
	# не трогаем и по дефолту next равен None.
	# Давайте представим что у нас уже создан один элемент
	# он и будет head ведь он вообще один. Теперь наша цель
	# это задать current_node и каждый раз менять его на
	# на следующий и так дойти до самого конца linked listа
	# к самому последнему элементу. Мы просто проверяем на
	# каждом current_node существует ли элемент после него.
	# Если существует, то переключает current_node на
	# следующий. А если нет, то цикл останавливается и
	# перед нами самый последний элемент. Теперь мы
	# должны задать элемент который будет идти после последнего
	# с помощью функции set_next которая принимает на вход целый node.
	# Тут же подход заключается в поиске самого последнего элемента
	# и когда он будет найден, добавить после него следующий. 
	def append(self, data):
		new_node = Node(data)
		current_node = self.head
		if current_node == None:
			self.head = new_node
			return
		while current_node.get_next() != None:
			current_node = current_node.get_next()
		current_node.set_next(new_node)

	# Небольшое отступление. Надо расставить все точки над и
	# и понять походы в методе __str__() и append(). И найти
	# их различия. Начем с того что представим linked list
	# с элементами 3 и 22. Как мы делаем в методе __str__()?
	# нам важно пройти с самого первого элемента по последний
	# соблюдая то что количетсво итераций должно совпадать с 
	# количеством элементов в linked listе. Мы смотри на то что
	# первый node не равен None и обновляем переменную и переходим
	# к следующему. Он тоже не равен Nonе, делаем все то же.
	# И вот уже следующий элемент равен None и его вообще
	# не существует. Видите, мы дошли до того пока current_nodе
	# не стал None. В методе append() это было бы нам вообще не на руку.
	# Именно поэтому мы и делаем проверку while current_node != None:
	# Давайте теперь разберемся со вторым методом.
	# В нем наша конечная цель это дойти до самого последнего
	# элемента и чтобы current_node им был. Для этого
	# мы делаем какбы подстраховку, а точнее смотрим на шаг впереди.
	# Стоя на 3, мы видим что 22 существует, поэтому задаем current_node в 22.
	# А вот уже следующей итерации не будет, ведь элемента
	# после 22 нет и он равен None. И когда наконец цикл прошел,
	# можно нормально поработать с current_node и все сделать.

	# empty() - bool returns True if empty
	# Тут все оооочень просто! Проверяем задан ли head.
	# Если не задан, то linked list пуст, если задан, то
	# в нем есть элементы.
	def empty(self):
		if self.head == None:
			print(True)
		else:
			print(False)

	# value_at(index) - returns the value of the nth item (starting at 0 for first)
	# Наша цель это пройти по каждому элементу
	# и на каждой итерации делаем проверку
	# совпадает ли искомый идекс с count.
	# Если да, то мы дошлм до искомого индекса
	# и выведем элемент по нему.
	# А если нет, то увеличим count и поменяет current_node.
	def value_at(self, index):
		current_node = self.head
		count = 0
		while current_node != None:
			if count == index:
				return current_node.data
			count += 1
			current_node = current_node.get_next()
		return "The value aat index haven't been found"

	# push_front(data) - adds an item to the front of the list
	# Тут алгоритм очень простой.
	# Создаем новый node на основе класса Node
	# куда передаем некоторую data.
	# Так же задаем current_node, это како бычно head.
	# Потом, с помощью метода set_next()
	# задаем то что current_node (изначальный head)
	# идет после new_node. И в конце задаем
	# новый head это будет new_node.
	def push_front(self, data):
		new_node = Node(data)
		current_node = self.head
		new_node.set_next(current_node)
		self.head = new_node

	# pop_front() - remove front item and return its value
	# Сначала мы проверим есть ли хоть один элемент
	# в нашем linked list. Если нету, то выведем ошибку.
	# А вот если есть, то мы задаим current_node он и есть head.
	# После этого зададим новый head который будет
	# элементов который идет после current_node.
	# Но вы спросите почему мы никак не удаляет элемент
	# а просто меняет переменные. Все просто. В питоне
	# элемент удаляется при компиляции если на него
	# не ссылается ни одна переменная. Тут мы больше
	# не ссылаем head на наш current_node. Поэтому
	# питон его удаляет.
	def pop_front(self):
		if self.head != None:
			current_node = self.head
			self.head = current_node.get_next()
		else:
			raise IndexError("Unable to pop from empty list")

	# pop_back() - removes end item and returns its value
	# Это уже третяя модификация while с current_node.
	# Изначально нам было не важно за current_node и он
	# вообще становился None. Потом в методе append мы 
	# шли с просмотром на шаг вперед и current_node становился
	# последним элементом. Тут же там нужен предпоследний
	# элемент и мы смотрим на два шага вперед!
	# И видим заранее когда у последний элемент ведет на None.
	# Останавливаемся именно на предпоследнем. И дошли до 
	# предпоследнего элемента ставим set_next() на None.
	def pop_back(self):
		current_node = self.head
		while current_node.get_next().get_next() != None:
			current_node = current_node.get_next()
		current_node.set_next(None)

	# front() - get value of front item
	# Ну тут все вообще понятно. Задаепм head_node
	# и возвращаем его значение.
	def front(self):
		head_node = self.head
		return head_node.data

	# back() - get value of end item
	# Тут уже известный вам алгоритм дохождения
	# до последнего элемента linked list.
	# Ну так вот, доходим и выводим значение data
	# этого последнего элемента.
	def back(self):
		current_node = self.head
		while current_node.get_next() != None:
			current_node = current_node.get_next()
		return current_node.data

	# insert(index, data) - insert value at index, 
	# so current item at that index is pointed to 
	# by new item at index
	# Ничего нового мы тут не делаем. Главное уловить суть.
	# Создаем с new_node с входной data, а так же создаем
	# current_node это head и ставим count = 0.
	# Потом запускаем цикл и current_node максимум может
	# быть только последним элементом поэтому проверяем
	# на шаг вперед. Кароче, чтобы добавить элемент по индексу
	# мы работает с ссылками на следующие элементы.
	# Мы наша задача установить current_node на элементе
	# индекс которого на один меньше заданного (index).
	# Каждую итерацию мы проверяем не осталась ли одна итерация
	# чтобы count стал равен index. Когда мы дошли до того места
	# где count на 1 меньше индекса, начинаем проделывать
	# наши грязные делишки. Сначала зададим в переменную
	# node который идет после current. Потом после current ставим new_node
	# а после new_node ставим the_node_after_current. Мы как бы 
	# встраиваем новый элемент между двумя стощими.
	# Если же index == 0, то просто вызывает функцию push_front()
	def insert(self, index, data):
		new_node = Node(data)
		current_node = self.head
		count = 0
		while current_node.get_next() != None:
			if index == 0:
				self.push_front(data)
				return
			elif count + 1 == index:
				the_node_after_current = current_node.get_next()
				current_node.set_next(new_node)
				new_node.set_next(the_node_after_current)
				return
			count += 1
			current_node = current_node.get_next()
		print("The index is out of range")

	# erase(index) - removes node at given index
	# Тут алгоритм ааааабсолютно такой же как и в предыдущем методе,
	# код отличается только в теле условия elif count + 1 == index:
	# У нас уже есть текущий node который стоит перед тем который нужно удалить
	# Мы должеы задать сам node который нужно удалить и node после него.
	# А дальше уже оперируем ссылками. node который перед тем 
	# который нужно удалить связывается с тем который после удаляемого.
	# Так как на удаляемый node нет ни одной ссылки, пайтон 
	# удаляет его при компиляции.
	# Если же index == 0, то просто вызывает функцию pop_front()
	def erase(self, index):
		current_node = self.head
		count = 0
		while current_node.get_next() != None:
			if index == 0:
				self.pop_front()
				return
			elif count + 1 == index:
				the_node_to_erase = current_node.get_next()
				the_node_after_erased = the_node_to_erase.get_next()
				current_node.set_next(the_node_after_erased)
				return
			count += 1
			current_node = current_node.get_next()
		print("The index is out of range")

	# reverse() - reverses the list
	# Это один из многих подходов.
	# Time Complexity: O(n) Space Complexity: O(1)
	# Этот способ мне нравится больше всего тк он оен понятный.
	# У нас есть три pointerа и мы передвигаем каждый по очереди.
	# Изначально prev и next равны None. А current_node равен head.
	# Первым делом распологаем next после current_node.
	# А затем уставливаем ссылку из current_node на prev
	# в самой первой итерации это None, но в последующих
	# prev будет идти за current_node.
	# Потом двигаем prev на current_node, а сам current_node
	# еще дальше на next и они совпадают. На этом 
	# итерация заканчивается. В итоге мы поменяли за одну итерацию
	# одну ссылку самого первого элемента. Но в последующих
	# будут менятся так по одному. Все закончится на том что
	# current_next дойдут до None и цикл остановится.
	# Только prev останется на последнем элементе.
	# Как итог, все элементы linked listа будут перевернуты.
	# Нам остается только изменить head, сделав его prev. 
	### Наглядно можно посмотреть тут: https://imgur.com/a/ETFBihl ###
	def reverse(self):
		prev = None
		current_node = self.head
		next = None
		while current_node != None:
			next = current_node.get_next()
			current_node.set_next(prev)
			prev = current_node
			current_node = next
		self.head = prev

