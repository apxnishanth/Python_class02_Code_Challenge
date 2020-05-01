def fibonacci(num):
    
    if num==0:
        return 0 
    
    if num==1:
        return 1
       
 
    return fibonacci(num-1)+fibonacci(num-2)


def lucas(num):
    
    if num==0:
        return 2
    
    if num==1:
        return 1
       
 
    return lucas(num-1)+lucas(num-2)    

def common_series(type,num):

     if type=='f':
        if num==0:
             return 0
        if num==1:
             return 1    
     if type=='l':
        if num==0:
             return 2
        if num==1:
             return 1
     return common_series(type,num-1)+common_series(type,num-2)                