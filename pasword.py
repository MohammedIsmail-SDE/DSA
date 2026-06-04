
name = input("please enter your name :")

if len(name )<3:
    print ("name must be above than 3 characters")
elif len(name)>50 :
    print ("name cannot be more than 50 characters")
else :
    print("Hi",name)
num = int (input ( "please enter weight : "))
units = input("This weight is in (L)bs or (k)g :")

if units.upper() == "L":
    converted = round(num *0.45,3)

    print(f'you are {converted} kilo')
else:
    converted = round(num / 0.45,3)
    print(f"your are {converted} pounds")