queue_list = []

# Добавление
queue_list.append(2)
queue_list.append(4)
queue_list.append(8)
queue_list.append(16)

# Удаление
queue_list.pop(0)
queue_list.pop(0)

# Вывод
print(queue_list)

# Минус в том что удаление из начала работает за O(n)