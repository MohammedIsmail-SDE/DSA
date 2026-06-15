def max_number(number):
    
    if not number :
        return None
    
    max_value = number [0]
    
    for nume in number :
        if nume >max_value :
            max_value = nume 
        return max_value
        
        
my_list= [1,2,5,8,99,66]
print(max_number(my_list))