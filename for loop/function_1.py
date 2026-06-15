def max_number(number):
    
    if not number :
        return None
    
    max_value = number [0]
    
    for nume in number :
        if nume > max_value :
            max_value = nume 
    return max_value
