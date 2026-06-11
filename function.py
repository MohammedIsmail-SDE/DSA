# def user_name(fristname,secondname):
#     print (f'Hi {fristname} {secondname}!')
    
# print("start")
# user_name("Mohammed","ismail")
# print("😊")


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