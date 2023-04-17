#Program to ind out compound interest
P= eval(input("plese enter the value of principal amount: "))
r= eval(input("plese enter the value of interest rate: "))
n= eval(input("plese enter the value of number of times interest applied per time period: "))
t= eval(input("plese enter the value of number of time periods elapsed: "))
A = P*(1+r/n)**(n*t)
print("The compound interest is: ",A)
