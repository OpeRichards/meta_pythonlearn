num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]

#8.  Finally, add a break statement directly after the print statement inside the if condition for finding the number. 
count = 0

for idx, item in enumerate(num_list):
    count += 1
    if item == 36:
        print('Number found at position: ', idx)
        break

print(count)
