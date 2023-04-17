""" def check_fun(a):
    if a>0:    
         print('True')
    else:
        print('False')
    
if __name__ == '__main__':
    s = input()
    
    if 0<len(s)<1000:
        sum_ch=0
        for ch in s:
            if ch.isalnum():
                sum_ch+=1
        check_fun(sum_ch)
        sum_ch=0
        for ch in s:
            if ch.isalpha():
                sum_ch+=1
        check_fun(sum_ch)
        sum_ch=0
        for ch in s:
            if ch.isdigit():
                sum_ch+=1
        check_fun(sum_ch)
        sum_ch=0
        for ch in s:
            if ch.islower():
                sum_ch+=1
        check_fun(sum_ch)
        sum_ch=0
        for ch in s:
            if ch.isupper():
                sum_ch+=1
        check_fun(sum_ch)
 """
 
def check_fun(a):
    if len(a) > 0: # if value is not None or empty    
        print('True')
    else:
        print('False')
    
if __name__ == '__main__':
    s = input()
    
    if 0<len(s)<1000:
        status = [ 1 for ch in s if ch.isalnum() ]
        check_fun(status)     
        
        
        check_fun([ ch for ch in s if ch.isalpha() ])
        check_fun([ ch for ch in s if ch.isdigit() ])        
        check_fun([ ch for ch in s if ch.islower() ])        
        check_fun([ ch for ch in s if ch.isupper() ])
        
        

