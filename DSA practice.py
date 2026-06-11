
def enmoji_Username():
    words = massage.split(' ')
    emojis = {
    ":)": "😊",
    ":(": "😢"
            }    
    output = " "
    for word in words:
        output += emojis.get(word, word) + " "
        

massage = input(">")
enmoji_Username(massage)

print(massage)  
