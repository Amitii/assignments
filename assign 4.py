# ASSIGNMENT 4
# QUESN 1 ( Tower of Hanoi)
def TowerOfHanoi(n , source, destination, auxiliary):
    if n==1:
        print ("Move disk 1 from source",source,"to destination",destination)
        return
    TowerOfHanoi(n-1, source, auxiliary, destination)
    print ("Move disk",n,"from source",source,"to destination",destination)
    TowerOfHanoi(n-1, auxiliary, destination, source)
         
# Driver code
n = 4
TowerOfHanoi(n,'A','B','C')
# A, C, B are the name of rods

# QUESN 2 (Pascal's Triangle)
# input n
n=5
for i in range(1, n+1):
    for j in range(0, n-i+1):
        print(' ',end='')

    # first element is always 1
    C=1
    for j in range(1,i+1):
        # first value in a line is always 1
        print(' ',C, sep='', end='')
        # using binomial coefficient
        C=C*(i-j)//j
    print()

#QUESN 3

int1,int2 = map(int,input("Enter 2 numbers: ").split())
Quotient = int1 // int2
Remainder = int1 % int2

#part <a>
print("a. Checking if the quotient and remainder is a callable value or not.")
print(callable(Quotient))
print(callable(Remainder))

#part <b>
if (Quotient == 0):
    print("<b> The quotient is zero")
if (Remainder == 0):
    print("<b> The remainder is zero")
if (Quotient !=0 and Remainder !=0):
    print("<b> All the values are non zero")

#part <c>
partClist = [Quotient + 4, Remainder + 4, Remainder + 5, Quotient + 5, Remainder + 5, Quotient + 6, Remainder + 6]

result = []
for i in range(len(partClist)):
    if partClist[i] > 4:
        result.append(partClist[i])
print(f"<c> Filtered out numbers that are greater than 4 are : {result}")

#part <d>
setresult = set(result)
print("<d> Set:",setresult)

#part<e>
immutableSet = frozenset(setresult)
#frozen set is used to make the set immutable
print("<e> Immutable set:", immutableSet)

#part<f>
print("<f> Hash value of the max value from the above set: ",hash(max(immutableSet)))


# QUESN 5

class Employee:
    def _init_(self, name, salary):
        self.name = name
        self.salary = salary
#creating employee records
employee1 = Employee("Mehak", 40000)
employee2 = Employee("Ashok", 50000)
employee3 = Employee("Viren", 60000)

# part <a>, updating salary
employee1.salary = 70000
print("(a) The updated salary of ",employee1.name,"is",employee1.salary)
# part <b>, deleting a record
print("(b) Record of Viren deleted" , end='')
del employee3


# QUESN 6
# inputting a word from the first friend
word = input("Enter the word: \n")
word=word.lower()

#inputting a meaningful word with the exact same letters
testword = input("Enter a new meaningful word using the exact same letters to test your friendship; \n")
testword=testword.lower()
#defining dictionary
def count_in_dict(word):
    count = {}
    list1 = list(word)

    n = len(list1)
    for i in range(n):
        if list1[i] in count:
            count[list1[i]] +=1
        else:
            count[list1[i]] = 1
    return count
#shopkeeper's input to verify the word's meaning
def userinput():
    if count_in_dict(word) != count_in_dict(testword):
        print("The letters are not exact,friendship is fake")
        return
    ans = input("Does the word make sense?(y/Y or n/N)")

    if ans == 'y' or ans== 'Y':
        print("The friends pass the friendship test")
    elif ans=='n' or ans=='N':
        print("The word doesn't have a meaning, friendship is fake")
    else:
        print("Invalid input, try again with y/Y or n/N ")
        userinput()
userinput()
























        


















