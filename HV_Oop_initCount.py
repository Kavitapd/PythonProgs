#countcreated instances of a class
class Person:
    count=0
    def __init__(self):
        Person.count=Person.count+1
        
    
    
p1=Person()    
p2=Person()
p3=Person()

print(Person.count)