

## Comparisons Practice: 


## Program: Determine if you are being productive or not. 


## Variables 

''' 

Input Resource Variables 
    Focus - percentage type 
    Attention -  percentage type 
    Time - int type 
    Energy - int type 

Output Resource Variables 
    Power - int type  
    Energy - int type 

'''

## is productive when input < output 

spent =  Focus * Attention * Time * Energy 

gained = Power + Energy   


def is_productive(spent, gained):

    if spent < gained:
        return True 

    return False







