#2d to 1d Array
matrix_1d=[]
matrix_2d=[[1,2,3],[4,5,6]]
for row in matrix_2d:
    for num in row:
        matrix_1d.append(num)
        print(matrix_1d)

# Remove vowel from sentence

vowels='aeiou'
sentence='I am  awesome'
filtered_letters=[]
for letter in sentence:
    if letter not in vowels:
        filtered_letters.append(letter)
        print(''.join(filtered_letters))


        #code with list comprehension
        vowels = 'aeiou'
        sentence = 'I am  awesome'
        filtered_letters_i = ''.join([letter for letter in sentence if letter not in vowels])
        print(filtered_letters_i)

#dictionary comprehension
#Create dictionary from two list
fruit_ranking=[1,2,3]
fruit_name=['mango','pineapple','watermelon']
fruit_rank_dict={}
for i in range(len(fruit_ranking)):
    fruit_rank_dict[fruit_ranking[i]]=fruit_name[i]
    print(fruit_rank_dict)


    #write this code using dictionary comprehension
    fruit_ranking_1=[1,2,3]
    fruit=['mango','pineapple','watermelon']
    fruit_rank_dict_1={fruit_ranking_1[i]:fruit[i] for i in range(len(fruit_ranking_1))}
    print(fruit_rank_dict_1)



