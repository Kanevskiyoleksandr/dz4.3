def my_function():
    print(" Задать длинну списка 1 ")
    a = int(input())
    print(" Задать максимальное значение в списке 1")
    b = int(input())
    from random import randint
    list1 = [randint(1, b) for i in range(a)]
    print(list1)

    print(" Задать длинну списка 2 ")
    c = int(input())
    print(" Задать максимальное значение в списке 2")
    d = int(input())
    from random import randint
    list2 = [randint(1, c) for i in range(d)]
    print(list2)

my_function()