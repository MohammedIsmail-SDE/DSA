# massage = input(">")
# words = massage.split(' ')
# emojis = {
#     ":)": "😊",
#     "):":"😥"
# }
# output =""
# for word in words :
#     output += emojis.get(word , word) + " "
# print(output)
massage = input(">")
words = massage.split(' ')

emojis = {
    ":)": "😊",
    ":(": "😢"
}

output = ""
for word in words:
    output += emojis.get(word,word) + " "

print(output)  # .strip() removes the trailing space
