# quesn 1
given="Python is a case sensitive language."
# part (a)
print(len(given))
# part (b)
print(given[::-1])
# part (c)
print(given[10:26])
# part (d)
print(given.replace("a case sensitive","object oriented"))
# part (e)
print(given.find("a"))
# part (f)
print(given.replace(" ",""))


# quesn 2
name= "Amiti"
SID= "21104011"
department= "EE"
CGPA= "9.9"
print("Hey!,"+name+" here!\n"+"My SID is "+SID+"\nI'm from "+department+" and my CGPA is "+CGPA)

# quesn 3
a=56
b=10
# part (a)
print(a&b)
# part (b)
print(a|b)
# part (c)
print(a^b)
# part (d)
print(a<<2)
print(b<<2)
# part (e)
print(a>>2)
print(b>>4)


# quesn 4
p=int(input("enter first no.: "))
q=int(input("enter second no.: "))
r=int(input("enter third no.: "))
largest=p
for i in[p,q,r]:
    if largest<i:
        largest=i
print("the largest no. is: ",largest)

# quesn 5
name=str(input("enter name: "))
found="no"
for i in['Mehak','Shruti','Disha','Abhishek','Harsh','Nishika']:
    if name==i:
         found ='yes'
print(found)

# quesn 6
a=int(input("1st side: "))
b=int(input("2nd side: "))
c=int(input("3rd side: "))
outcome='NO'
if (a+b>c) & (b+c>a) & (c+a>b):
    outcome='yes'
print(outcome)    








