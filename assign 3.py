# ASSIGNMENT 3
# Quesn 1
# Counting occurences of a character in a string
string=input("Enter string: ")
char=input("Enter the character to be counted: ")

count=0
for i in range(len(string)):
    if(string[i]== char):
        count=count+1

print(char+" has occured= "+str(count)) 
        
# Quesn 2
# Printing next date of input date
year=int(input("Enter year[1800-2025]: "))
#writing the conditions of a leap year.
if (year % 400 == 0):
    leap_year=True  
elif(year%100==0):
    leap_year=False
elif(year%4==0):
    leap_year=True
else:
    leap_year=False

month=int(input("Enter a month[1-12]: "))
#writing the conditions of 30,31,28/29 days of a month
if month in (1,3,5,7,8,10,12):
    month_length=31
elif month==2:
    if leap_year:
        month_length=29
    else:
        month_length=28
else:
    month_length=30

day=int(input(" Enter a day [1-31]: "))
#writing the conditions when input date is last date of month
if day < month_length:
    day +=1
else:
    day=1
    if month==12:
        month=1
        year +=1
    else:
        month +=1
print("Next date of input date is [dd-mm-yyyy]%d-%d-%d. " % (day, month, year))


# Quesn 3
# Creating list of tuples with 1st element as the number and seccond element as square of the number.
original_list=[3, 9, 10]
square_list=[]
for i in original_list:
    square_tuple=(i,i**2)
    square_list.append(square_tuple)
print(square_list)
# Quesn 4

marks=int(input("Marks"))

if(marks>=4 and marks<=10):
    if(marks==4):
        grade="D"
        perform="poor"
    elif(marks==5):
        grade="C"
        perform="below average"
    elif(marks==6):
        grade="C+"
        perform="average"
    elif(marks==7):
        grade="B"
        perform="good"
    elif(marks==8):
        grade="B+"
        perform="very good"
    elif(marks==9):
        grade="A"
        perform="excellent"
    elif(marks==10):
        grade="A+"
        perform="outstanding"
else:
    print("error")

print("Your grade is " +str(grade)+" and your performance is "+ perform +".")

# Quesn 5
n=int(input("number: "))

a_to_k="ABCDEFGHIJK"

for i in range(n):
    if 2*i<n:
        j=a_to_k[:n-2*i]

        print(" "*i,j)
    

#Quesn 7
def fibo(n):
    if n==1 or n==2:
        return 1
    return fibo(n-1)+fibo(n-2)
n=int(input("Enter n\n"))

j=0

for i in range(1,n+1):
      print(f"{fibo(i)}",end=",")
      j=j+fibo(i)

print(end="\n")
print(j/n)

#Quesn 8
set1={1,2,3,4,5}
set2={2,4,6,8}
set3={1,5,9,13,17}

set_a=(set1 | set2) - (set1 & set2)
print("part a: ",set_a)

set_b=(set1|set2|set3)-(set1&set2)-(set2&set3)-(set3&set1)
print("part b: ",set_b)

set_c=(set1&set2)|(set2&set3)|(set3&set1)-(set1&set2&set3)
print("part c: ",set_c)

list_d=[]
for i in set1:
      if i>=1 and i<=10:
       list_d.append(i)
set_d=set(list_d)
print("part d: ",set_d)

list_e=[]
for i in (set1|set2|set3):
      if i>=1 and i<=10:
       list_e.append(i)
set_eout=set(list_e)
print("part e: ",set_eout)



#QUESN 6
dict1 = {}
while True:                                                                                                         #Loop for inputting values
    name = input("Enter the name of the student: ")
    SID = int(input("Enter the SID of %s: " % name))
    dict1[SID] = name
    print("\nYou have entered %d value(s) till now" % len(dict1))
    while True:
        more_data = input("Do you want to enter more data? ")
        if more_data in ("N","n","No","no","NO"):
            more_data = 0
            break
        elif more_data in ("Y","y","Yes","yes","YES"):
            more_data = 1
            break
        else:
            print("\nPlease say yes or no")
            continue
    if more_data == 0:
        break
print("\na. Student Details:")                                                                                      #Q6(a)
for i in dict1:
    print("The SID of \033[1m%s\033[0m is \033[1m%d\033[0m" % (dict1[i],i))
dict2 = {}
for sorted_value in sorted(dict1.values()):                                                                         #Sorting the dictionary using student names
    for key,value in dict1.items():
        if value == sorted_value:
            dict2[key] = value
print("\nb. Student Details (sorted with respect to names):")                                                       #Q6(b)
for i in dict2:
    print("The SID of \033[1m%s\033[0m is \033[1m%d\033[0m" % (dict2[i],i))
dict3 = {}
for sorted_key in sorted(dict1):                                                                                    #Sorting the dictionary using SIDs
    for key,value in dict1.items():
        if key == sorted_key:
            dict3[key] = value
print("\nc. Student Details (sorted with respect to SIDs):")                                                        #Q6(c)
for i in dict3:
    print("The SID of \033[1m%s\033[0m is \033[1m%d\033[0m" % (dict3[i],i))
print("\nd. ", end="")                                                                                              #Q6(d)
while True:
    search_SID = int(input("Enter the SID of the student: "))
    if search_SID in dict1:
        print("The name of student whose SID is %d is \033[1m%s\033[0m" % (search_SID,dict1[search_SID]))
        break
    else:
        print("The SID you entered isn't entered\nPlease enter a valid SID to be searched\nList of valid SIDs: %s\n" % list((dict1.keys())))
        continue







