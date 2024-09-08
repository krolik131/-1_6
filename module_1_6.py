my_dict = {'Kostya': 1984, 'Dima': 1990, 'Yuliya' :1991} #Создаём словарь
print(my_dict) # Выводим словарь на экран
print(my_dict['Kostya']) #Выводим на экран одно значение по существующему ключу
print(my_dict.get('Yana')) # Выводим на экран одно значение по отсутствующему ключу
my_dict.update({'Kolya': 2000,
                'Olga'  : 1999}) # Добавим ещё две пары
print(my_dict)
print(my_dict.pop('Kostya')) # Удаляем одну пару
print(my_dict) # Выводим на экран словарь

my_set = {1,2,3,1,2,True,'String'} # Создаём множество
print(my_set) # Выводим на экран
my_set.add(7) # Добавляем элемент
my_set.add(9) # Добавляем элемент
my_set.discard('String') # Удаляем строковый элемент
print(my_set) # Выводим на экран измененное множество