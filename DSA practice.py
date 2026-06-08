num_1 = [1,2,3,3,4,4,5,5,9,2]
num_2= []
for number in num_1:
    if number not in num_2:
        num_2.append(number)
print(num_2)