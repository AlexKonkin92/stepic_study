#Напишите функцию update_dictionary(d, key, value), которая принимает на вход словарь d и два числа: key и value.
#Если ключ key есть в словаре d, то добавьте значение value в список, который хранится по этому ключу.
#Если ключа key нет в словаре, то нужно добавить значение в список по ключу 2 * key.
#Если и ключа 2 * key нет, то нужно добавить ключ 2 * key в словарь и сопоставить ему список из переданного элемента [value].

d = {}
def update_dictionary(d, key, value):
    if key in d: #если ключ есть в словаре
        d[key].append(value) #добавляем к этому ключу значение
    elif key not in d and key * 2 in d:#второе условие на поиск ключа в словаре
        d[key * 2].append(value)
    elif key * 2 not in d:#если ничего из этого нет
        d[key * 2] = [value]#добавляем новый ключ и значение
print(update_dictionary(d, 1, -1))#все, что ниже для примера
print(d)
update_dictionary(d, 2, -2)
print(d)
update_dictionary(d, 1, -3)
print(d)
