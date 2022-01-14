# assignment 1
# ques 1
a=67
b=12
c=76
average=(a+b+c)/3
print(average)

# ques 2
tr=0.2 #tr=tax rate=20%=0.2 (given)
sd=10000 #sd=standard deduction in dollars(given)
dd=3000 #dd=dependent deduction in dollars (given)
gi=1000000 #gi=gross income in dollars (user input)
nd=4 #nd=number of dependents (user input)
#calculating taxable income(ti)
ti=gi-sd-(dd*nd)
print(ti)
#calculating tax
tax=ti*tr
print(tax)

# ques 3
name=input('name: ')
sid=int(input('SID: '))
gender=input('gender: ')
course=input('Course name: ')
CGPA=input('CGPA: ')
Student=[sid,name,gender,course,CGPA]
print(Student)

# ques 4
M1=int(input('Marks of 1st student ')
M2=int(input('Marks of 2nd student ')           
M3=int(input('Marks of 3rd student ')
M4=int(input('Marks of 4th student ')        
M5=int(input('Marks of 5th student ')
Marks=[M1,M2,M3,M4,M5]
Marks.sort()
print(Marks)

# ques 5
color=['Red','Green','White','Black','Pink','Yellow']
print(color)
# a part
del color[3]
print('After deleting 4th item, list is: ',color)
# b part
color=[3]=color[4]='purple'
print('Answer for part B: ',color[0:4]+color[5: ])
