#program to input name and n subject marks and calculate total average.
name=input("Enter name of student: ")
sub=int(input("enter number of subjects: "))
marks=[]
for i in range(sub):
    m=int(input("Enter marks: "))
    marks.append(m)
print("Name of the student: ",name)
print("marks: ",marks)
print("Total marks: ",sum(marks))
print("Average is:",sum(marks)/sub)
