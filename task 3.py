# Определить, является ли год, который ввел пользователем, високосным или невисокосным
# В соответствии с григорианским календарем, год является високосным, если его номер кратен 4, но не кратен 100, а также если он кратен 400.

g = int(input('введите год: '))

if g % 400 == 0:
    print('этот год високосный')
elif g % 4 == 0 and g % 100 != 0:
    print('этот год високосный')
else:
    print('этот год невисокосный')
