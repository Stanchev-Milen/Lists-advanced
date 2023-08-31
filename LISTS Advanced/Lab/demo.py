def my_list_fx():
    my_list = [i if i % 2 == 0 and i != 0 else False for i in range(my_input)]
    return my_list        # ако не му кажеш какъв да е ритърна ще ти върне просто 'None'


my_input = int(input("Enter a number: "))
return_list = my_list_fx()
print(return_list)
