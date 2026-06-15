import maximum_function

input_number = input("Please Enter Numbers :-")

numbers = [ int (x) for x in input_number.split()]

print(maximum_function.max_number(numbers))