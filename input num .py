phone =input("Enter Phone Number : ")
dig ={
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four",
    "5":"five"
}
output =""
for ch in phone:
        output += dig.get(ch,"!") + " "
print(output)