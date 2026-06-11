
def enmoji_Username():
    words = massage.split(' ')
    emojis = {
    ":)": "😊",
    ":(": "😢"
            }    
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
        return output
        
        
massage = input(">")
print(enmoji_Username(massage))  
