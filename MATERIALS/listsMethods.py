my_list = [1, 2, 3, 4]

# append
my_list.append(5)
print("After appending element at the end: " + str(my_list))

# extend
my_list.extend([6, 7, 8])
print("After extending array with another array: " + str(my_list))

# insert
my_list.insert(5, 20)
print("Inserted 20 at index 5: " + str(my_list))

# remove
# Удаляет первую найденную слева направа
my_list.remove(20)
print("Remove first founded element that is 20: " + str(my_list))

# pop
my_list.pop()
my_list.pop(2)
print("After removing last and by index 2: " + str(my_list))

# index
# возвращает идекс элементв
print("The index of 7 is " + str(my_list.index(7)))

list1 = [1, 2, 3, 4, 1, 1, 1, 4, 5]

# Will print index of '4' in sublist
# having index from 4 to 8.
print(list1.index(4, 4, 8))

# Will print index of '1' in sublist
# having index from 1 to 7.
print(list1.index(1, 1, 7))

# count
print("Two accures: " + str(my_list.count(2)) + " times")

# clear
my_list.clear()
print("The result after .clear(): " + str(my_list))
