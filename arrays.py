numbers = [10,20,30,240,90]


#get item if you know the index
print(numbers[0])


##get out element array
#for num in numbers:
#    print(num)
#
#for i in range(len(numbers)):
#    print(numbers[i])

##update array
#numbers[0]='name'
#print(numbers)


#linear serach
num = numbers[0] # Sets num to the first element.

for element in numbers: # Loops over each element.
    if element > num: # Checks if the current num is less than an element
        num = element # Switches the old num to the num value

print(num) # Prints num

