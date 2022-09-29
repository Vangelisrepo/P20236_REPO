lst1 = "753"
t1= 548
numbers =[]
def thresh(some_string,t1,idx = 0):
    
    if idx == len(some_string) - 1:       
        str = "".join(some_string)
        if int(str) > t1:
          print(str)
        
        
        
        
        
      
        
        
    for j in range(idx, len(some_string)):
        numb_list = [c for c in some_string]   
        numb_list[idx], numb_list[j] = numb_list[j], numb_list[idx]
        thresh(numb_list,t1,idx+1)
        
    
        

thresh(lst1,t1)
