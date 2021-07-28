# Создание словаря
slovar = {"StrVal": "SomeStr", "BoleanVal": True, "IntVal": 228}

# Вывод словаря
print(slovar)

# Вывод keys и values отдельно
print(slovar.keys())
print(slovar.values())

# Добавить новый элемент
slovar["NewEl"] = 4127

# Вывод value по заданному key
print(slovar["NewEl"])

# Удаление элемента по заданному key
del slovar["NewEl"]

# Преобразование словаря в list
print(list(slovar)) # По дефолту берутся только keys
print(list(slovar.keys())) # Это можно увидеть тут
print(list(slovar.values())) # Но так же можно и с values

# Сортировка словаря
# Сначала преобразовывает в list
# сортирует srt по первый букве
# а int по возрастанию
# Так же можно добавить .keys() или .values()
print(sorted(slovar))

# Так же как и с list
# Проверка на наличие элемента в словаре
print("StrVal" in slovar)
# Или так
print("StrVal" not in slovar)

# Можно создавать словари более удобным способом
new_slov = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
new_slov["audi"] = 1111 # Добавление нового элемента
new_slov["cars", 12] = 121212 # Илииии
print(new_slov)

# Есть и еще один способ когда все keys это str
str_slov = dict(sape=4139, guido=4127, jack=4098)
print(str_slov)
