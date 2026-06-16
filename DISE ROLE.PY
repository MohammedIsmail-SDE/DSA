import random 
class Dise :
    def role (self):
        frist=random.randint(1,6)
        second=random.randint(1,6)
        return frist,second
    
    
dise = Dise ()

print(dise.role())
        


