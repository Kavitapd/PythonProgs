# program to convert temperature to and from celcius, farenheit
c_temp = eval(input("Enter temp in celcius: "))
f_temp = (c_temp * 9/5) + 32
print("Temp in farenheit is: ", f_temp)
f_temp = eval(input("enter temp in Farenheit: "))
c_temp = (f_temp-32)*5/9
print("Temp in celcius is: ", c_temp)

