import os
import socket
x=10
y=20
x,y=y,x
print(x,y)
#Reverse a string in python
a="I love to play cricket"
print("Reverse the string:",a[::-1])

#Print The File Path Of Imported Modules.

print(os)
print(socket)
#Use Of Enums In Python.

class MyName:

    Geeks, For, Geeks = "rony","tarq","sabbir"

print(MyName.Geeks)
print(MyName.For)
print(MyName.Geeks)
#return multiple value from function
 def q():
    return 1, 2, 3, 4
a, b, c, d = q()

print(a, b, c, d)