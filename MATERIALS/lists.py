# Списки - это упорядоченные, изменяемые коллекции 
# объектов произвольных типов

# В Python как таковых массивов не существует, 
# вместо них используются списки

# Чтобы создать список, нужно
# заключить все входящие в него элементы в []
# и разделить их запятыми

mylist = [1, 2, 3, 4]
print(mylist)

# Списки могут содержать разные типы данных

various_list = [10, "test", True]
print(various_list)

# Так же списки могут быть вложенные
# это помагает в работе с интернет запросами

vloj_list = ["some text", ["vlojenniyy text", "another one"]]
print(vloj_list)

# Еще один способ создать список
# Он более полный
second_method_list = list([1, 2, 3])
print(second_method_list)

# Прикольные методы в Python
print(list("Roma")) # Разбивает любой итерируемый обьект и складывает в список
print(len(mylist)) # Так же как и со строками, выдает количество элементов
print(mylist[1:3]) # Тоже что-то типа срезов с строках

mylist[0] = 20 # В отличае от строк, в списках можно изменять определенные элементы
print(mylist)

mylist.append(228) # Добавление значения в конец списка
mylist.append([21, 22, 23]) # Добавление списка в конец списка
print(mylist)

mylist.extend([2020, 2021]) # Обьединение двух списков. Значения списка в функции идут в конец
print(mylist)

mylist.pop() # Удаление последнего элемента в списке
mylist.pop(0) # Удаление первого элемента (Так можно с любым)
print(mylist)

mylist.reverse() # Переворачивает список
print(mylist)

int_list = [3, 2, 1]
str_list = ["aaa", "cccc", "bb"]
int_list.sort() # Отсортировывает список по увеличение чисел
str_list.sort() # Отсортировывает список в алфавитном порядке
print(int_list)
print(str_list)

list_in_list = [1, 2, [3, 4], 5]
print(list_in_list[2][1]) # Получение значения вложенного списка

# Способ работы с Матрицами
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Создаем матрицу

# 123
# 456
# 789

second_collumn = [row[1] for row in matrix] # Со списками мы можем применять циклы
print(second_collumn)


#### Присвоение списков ####
list1 = [1, 2, 3] # Задаем список list1
list2 = list1 # Задаем список list2 и присваиваем ему значение list1

list1[0] = 6 # Меняем первое значение list1 на 6

# Выведем результат
print(list1)
print(list2)

# Мы увидим что вывод list1 и list2 будет одинаковым.
# Все потому что при присвоении одного саиска другому list2 = list1
# list2 получает не значения list1, а ссылку на него.
# Как уже известно, ссылки на обьекты хранятся в памяти
# и переменные ссылаются на них

# Точно так же и с переменными

