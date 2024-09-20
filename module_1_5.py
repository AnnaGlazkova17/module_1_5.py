# module_1_5
immutable_var = 1,'Привет',3.14,'Hello',True # кортеж содержит int, str, float, boolean
# immutable_var [0] = 101 - нельзя изменить элемент кортежа, т.к. кортеж относится к неизменяемым типам
print('Immutable tuple:', immutable_var) # вывод кортежа на экран
mutable_list= ['Я',1,'делаю шаг, делаю',2,False] # создала список
mutable_list[-1]= True
print('Mutable list:',mutable_list)