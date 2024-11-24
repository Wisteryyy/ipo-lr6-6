import random # библиотека random

random_tuples = [tuple(random.randint(-10, 10) for _ in range(4)) for _ in range(20)] # список из 20 кортежей, каждый из которых содержит 4 случайных числа в диапазоне от -10 до 10

unique_tuples_set = set(random_tuples) # множество уникальных комбинаций кортежей
unique_tuples_list = list(unique_tuples_set) # преобразуем множество в список
print(f"Уникальные комбинации: {unique_tuples_list}") # выводим

number = int(input("Введите целое число: ")) # запрашиваем ввод числа

count = 0  # переменная для количества
for current_tuple in unique_tuples_list: # перебираем каждый кортеж в списке уникальных комбинаций
    if sum(current_tuple) < number: # проверка условия
        count += 1 # увеличиваем счетчик на 1, если условие истинно

print(f"Количество кортежей, чья сумма меньше заданного пользователем значения: {count}") # выводим
