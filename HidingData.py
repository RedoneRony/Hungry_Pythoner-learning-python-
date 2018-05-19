class MyClass:
    # Hidden member of MyClass
    __hiddenVariable = 0

    # A member method that changes
    # __hiddenVariable
    def add(self, increment):
        self.__hiddenVariable += increment
        print(self.__hiddenVariable)


# Driver code
myObject = MyClass()
print(myObject._MyClass__hiddenVariable)
myObject.add(2)
myObject.add(5)

# This line causes error
print(myObject._MyClass__hiddenVariable)
