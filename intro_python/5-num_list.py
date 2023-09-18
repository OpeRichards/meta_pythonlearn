num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]

#5.  Next, create a new variable called count and assign it a value of 0 and place it outside the for loop.
#6.  Inside the for loop increment the counter by 1.
#7.  Add a print statement outside the for loop to print the value of the count variable.
count = 0
for idx, item in enumerate(num_list):
    count += 1
    if item == 36:
        print('Number found at position: ', idx)

print(count)
