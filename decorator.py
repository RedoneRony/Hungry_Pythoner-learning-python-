# def div(a,b):
#     print(a/b)
#
# div(2,4)


# def div(a,b):
#     if a<b:
#         a,b = b,a
#     print(a/b)
#
# div(2,4)

def div(a,b):
    print(a/b)

def smart_div(func):

    def inner(a,b):

        if a<b:
            a,b = b,a
        return func(a,b)

    return inner

div = smart_div(div)

div(2,4)
