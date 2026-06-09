words = massage.split(' ')
emojie = {
    ":)": "😊",
    "):":"😥",
}
output =" "
for word in words :
    output += emojie.get(word,word) + " "
    print(output)