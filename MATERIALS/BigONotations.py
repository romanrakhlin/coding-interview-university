# Будем разбирать Time Complexity, а именно
# наиболее распрастраненные Big O Notations.
# Разбор по видосу - https://www.youtube.com/watch?v=V6mKVRU1evU
# Импортируем библиотеку для расчета времени работы алгоритмов
# и задаим нужные переменные.

import time

arr = []
size = 0
items = 0

def generateArray(n):
    new = []
    for i in range(1, n + 1):
        new.append(9)
    return new

# O(1)

# Это что-то очень простое, для чего не нужно выделять место в памяти
# И алгоритм выполняется мнгновенно.

def addItemToArray(item):
    arr.append(item)

def showTheLengthOfArray():
    print(len(arr))

# O(n)
print("Test of O(n)")
# Чем больше размер рассматриваемых данных, тем дольше работает алгорим.
# То есть, идет линейное увеличение на одно и то же значение к бесконечности.
# Для примера, напишам функцию, которая будет искать определенное значение в массиве,
# и когда найдет выведет индекс на котором стоял найденный элемент и время, за которое был совершен этот линейный поиск.
# Будем тестироват с массивами с самыми худшими вариантамии, где искомое значение стоит в самом конце.

def linearSearchForValue(value):
    startTime = time.time()
    foundAtIndex = 0

    for i in range(len(arr)):
        if arr[i] == value:
            foundAtIndex = i

    endTime = time.time()
    print(foundAtIndex, endTime - startTime)

arr = generateArray(1000)
arr.append(1)
linearSearchForValue(1)

arr = generateArray(10000000)
arr.append(1)
linearSearchForValue(1)

print()

# В результате видим разницу по времени. Даже не повыведенному,
# а по запуску видно, что первый отвыет вывелся мнгновенно.

# O(n^2)
print("Test of O(n^2)")
# Время, за которое алгоритм данной сложности выполнится, будет
# пропорционально квадрату данных, которые алгоритм принрмает на вход.
# Тут в пример идеально подходит Bubble Sort

def bubbleSort(array):
    testArr = array
    startTime = time.time()
    n = len(testArr)

    for i in range(n - 1):
        for j in range(n - i - 1):
            if testArr[j] > testArr[j + 1]:
                testArr[j], testArr[j + 1] = testArr[j + 1], testArr[j]

    endTime = time.time()
    tookTime = endTime - startTime

    return tookTime

arr = generateArray(1000)
arr = bubbleSort(arr)
print(arr)

arr = generateArray(10000)
arr = bubbleSort(arr)
print(arr)

print()

# Как можно видеть, то выполнение второго теста очень долгое.
# Хотя мы не как в тестах на O(n) ставили миллион элементов массива.
# Мы поставили лишь 10000. И разница в первом и втором тестах просто коллосальная!
# Это повод не использовать данную сложность в своих алгоритмах,
# ведь видно как жестко увеличивается время работы.
# Но опять же, O(n^2) можно использовать вместо O(n) если
# количество вводимых данных не очень большое.

# O(log n)
print("Test of O(log n)")

# Данная сложность лучше линейной, так как работает быстрее
# и работает с меньшим количеством данных.
# Для примера реализуем стандартный Бинарный Поиск.
# Не будем в даваться подробности, тк будем разбирать это позднее.
# Но вывод будет таким что сначала выведем количество захождений в массив,
# потом индекс на котороми стояло искомое значение и потом время которое ушло на работу алгоритма.

def binarySearchForValue(value):
    startTime = time.time()
    arr.sort()

    lowIndex = 0
    hightIndex = len(arr) - 1

    timesThrough = 0
    foundAtIndex = 0

    while lowIndex <= hightIndex:
        middleIndex = (hightIndex + lowIndex) // 2

        if arr[middleIndex] < value:
            lowIndex = middleIndex + 1
        elif arr[middleIndex] > value:
            hightIndex = middleIndex - 1
        else:
            foundAtIndex = middleIndex
            lowIndex = hightIndex + 1

        timesThrough += 1

    endTime = time.time()
    tookTime = endTime - startTime

    print(timesThrough, foundAtIndex, tookTime)

arr = generateArray(1000)
arr.append(10)
binarySearchForValue(10)

arr = generateArray(10000000)
arr.append(10)
binarySearchForValue(10)

print()

# Видим, что время показывается не очень точно, но при установке за 10 000 000
# заметна разница в работе первого и второго примеров.
