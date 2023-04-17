class Date:
    def __init__(self,d,m,y): #constructor
        self.__dd=d #private instance varriable
        self.__mm=m
        self.__yy=y
    def getYear(self):      #instance method
        return self.__yy
    def getMonth(self):
        return self.__mm
    def getDate(self):
        return self.__dd
    def setYear(self,y):
        self.__yy=y
    def setMonth(self,m):
        self.__mm=m
    def setDate(self,d):
        self.__dd=d

def main():
    dob=Date(10,12,18)
    print(dob.getDate())
    d=dob.setDate(18)
    print(dob.getDate())
main()