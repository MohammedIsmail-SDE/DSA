class Person:
    def talk(self):
        human = {
            "hi": "Hello",
            "how are you": "im fine "
        }
        user = input(">")
        return human.get(user, "I don't understand")
    
    user =input(">")
    print(user)