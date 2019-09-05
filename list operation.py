#list slice
some_marks= [2,4,5,6,7,8,9]

avg_marks=some_marks[4:8]
print(avg_marks)

#Index jump

numbers=[1,2,3,4,5,6,7,8,9,10]
print(numbers[1:9:2])

#negative index slice
squares=[1,2,3,4,5,6,7,8,9,10]
print(squares[2:-2])
print(squares[::-1]) #list reverse

#some numeric operations of list
print(sum(numbers))
print(min(numbers))
print(max(numbers))
