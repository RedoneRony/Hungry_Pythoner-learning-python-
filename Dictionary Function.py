'''Access the data using key and get'''
my_list=[2,3,4,5]
print(my_list[3])


my_list[3]=6
print(my_list[3])

nums={1: "one", 2:"two",3:"three"}

print(4 in nums)

print(nums.get(5, "5 is not in the nums"))
