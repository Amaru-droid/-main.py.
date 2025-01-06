immutable_var = tuple_ = (1 , 3 , 'string')
print (immutable_var) #  Операция вывода кортежа immutable_var на экран.
# immutable_var = [0] = 4 # Попытка изменить элементы кортежа immutable_var.Ошибка сообщает о том, что кортеж не поддерживает обращение по элементам
mutable_list = tuple_1 = ([1 , 3 , 5] , 7,) # mutable_list из нескольких элементов.
print (mutable_list)
mutable_list [0][0] = 4 # Изменение элементов списка mutable_list
print (mutable_list) # Измененный список mutable_list