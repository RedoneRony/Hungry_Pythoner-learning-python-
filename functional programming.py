from typing import Any, Tuple, Callable, Union

'''
def make_twice(func, arg):
    return func(func(func(arg)))
def add_five(x):
    return x + 5

print(make_twice(add_five, 10))

#impure function

my_list = []
def my_impure_function(arg):
    my_list.append(arg)
    my_impure_function(10)
    print(my_list)
'''
def my_function(func, arg):
    return func(arg)

    print(my_function(lambda X: 2* X,5))
    print(a)

    print((lambda  x,y: x+ 2 * y)(2,3))