"""
input:
getCurrency
getLongAccountNumber
getLoanID
getSWIFTCode
get space if character is in uppercase followed by lowercase
get space if character  in lowercase is followed by uppercase



"""

def getUserFriendlyName(methodName):
    name=methodName[3:]
    newName=''
    for idx in range(len(name)):        
        if 0<idx<len(name)-1:
    
            if  (name[idx].isupper() and name[idx-1].islower()) or (name[idx].isupper() and name[idx+1].islower()):
                newName= newName+'_'
            
        newName= newName + name[idx]
    return newName 

methodNames=['getCurrency',
'getLongAccountNumber',
'getLoanID',
'getSWIFTCode']
for methodName in methodNames:    
    ufName=  getUserFriendlyName(methodName)
    print(ufName)
    