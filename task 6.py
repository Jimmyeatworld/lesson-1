#Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

x = int(input('введите номер буквы: '))

y = ord('a') + x - 1

z = chr(y)

print(f'это буква: {z}')