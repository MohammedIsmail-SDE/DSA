massage = input(">")
words = massage.split(' ')
emojie = {
    ":)": "😊",
    "):":"😥",
}
output =" "
for word in words :f
    output += emojie.get(word,word) + " "
print(output)
