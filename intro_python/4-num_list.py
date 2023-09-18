num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]

#Update the for loop to use the enumerate function so you can get and use the index. Alter the condition to look for number 36 and print out the following: ‘Number found at position: ‘, index number
for idx, item in enumerate(num_list):
    if item == 36:
        print('Number found at position: ', idx)
