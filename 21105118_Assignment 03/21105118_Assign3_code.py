#Que1'Code
print ("Que1 - Output\n")

#defining a function which return then occurance
def occur():
    #taking string input from the user
    para = input("Enter the String : ")

    #Checking if the string contains one or more words
    if " " in para:
        #splitting the string and storing it in an list
        sp = para.split()
        smlcase = [] #creating empty list
        dict = {} #creating empty dictionary

        #iterating in the splitted list and storing each iterated values in new list by lowercasing it
        for val in sp:
            val = val.lower()
            smlcase.append(val)

        #converting list to set to avoid similar entries
        unqsml = set(smlcase)

        #iterating in set
        for char in unqsml:
            count = smlcase.count(char)
            dict[char] = count #storing each iterated value and it's count as key-value pair

    else:

        #lowercasing inputted string
        para = para.lower()
        smlcase = [] #creating empty list
        dict = {} #creating empty dictionary

        #iterating in inputted string and appending each iteratied value in new list by lowercasing it
        for char in para:
            smlcase.append(char)

        # converting list to set to avoid similar entries
        unqsml = set(smlcase)

        # iterating in set
        for val in unqsml:
            count = para.count(val)
            dict[val] = count #storing each iterated value and it's count as key-value pair

    print("Dictionary containing {'Letter':'Letter Count'} is : %s" % (dict))

#calling the function
occur()

#Que2'Code
print ("Que2 - Output\n")

#defining a function which checks for leap year and returns an boolean output
def checkyear(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
             return True
    else:
        return False

#defining a function which determines the length of month
def len(month):
    if month in (1, 3, 5, 7, 8, 10, 12):
         return 31
    elif month == 2:
        # checking for the leapyear using checkyear() function defined above to determine month length
        isleap = checkyear(year)
        if isleap:
            return 29
        else:
            return 28
    else:
        return 30

#defining a function which checks for Validity of the input values
def isvalid():
    if day >= 1 and day <= 31:
        if month >= 1 and month <= 12:
            if year >= 1800 and day <= 2025:
                return True
    else:
        return False

#taking inputs from the user
day = int(input("Enter the day [1-31] : "))
month = int(input("Enter the month [1-12] : "))
year = int(input("Enter the year [1800-2025] : "))

#calling len() function defind above
month_len = len(month)

#Checking Validity of the input using isvalid() function defined above by calling it
bool = isvalid()
temp = 1

#modifying values for next date
if day < month_len:
    day += 1
elif day == month_len:
    day = 1
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1
else :
    temp = 0

#printing next date for valid input
if bool == True and temp == 1:
    if month < 10:
        print("Next Date is: %s/0%s/%s." % (day, month, year))
    else:
        print("Next Date is: %s/%s/%s." % (day, month, year))
else:

    #Displaying Warning for Invalid Inputs
    print("Invalid Input Values")

#Que3'Code
print ("Que3 - Output\n")

#creating empty list
list = []
print("Instruction! Press X or x to exit")
while True:
    temp = input("Enter any Digit : ")
    if temp == "x" or temp == "X":
        break
    #taking input from the user and appending it to list as int
    list.append(int(temp))

#creating empty list
newlist = []
for i in list:
    tup = (i,i*i)
    newlist.append(tup)

#displaying required output
print(newlist)

#Que4'Code
print ("Que4 - Output\n")

#taking input from the user
gd = int(input("Hey User, Enter the grade : "))

#storing givendata in dictionaries
letter_grade = {10 : "A+",9 : "A",8 : "B+",7 : "B",6 : "C+",5 : "C",4 : "D"}
performace = {10 : "Outstanding",9 : "Excellent",8 : "Very Good",7 : "Average",6 : "C+",5 : "Below Average",4 : "Poor"}

#Checking for validity of grade
if gd >= 4 and gd <=10:
    # Displaying result message
    print("Your grade is '%s' and %s Performance." % (letter_grade[gd], performace[gd]))
else:
    #displaying Warning for invalid input
    print("invalid grade")

#Que5'Code
print ("Que5 - Output\n")

char= ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']

for row in range(6):   #As there are '6' rows
    col=0
    counter=0
    while col<11:     #As there are '11' columns from A to K
        if col<row or col>11-row-1:
            print(" ", end="")

        else:
            print(char[counter], end="")
            counter=counter+1
        col= col + 1
    print("")

#Que6'Code
print ("Que6 - Output\n")

# creating empty dictionaries
dict1, dict2 = {}, {}
while True:

    #Taking input from the User
    name = str(input("Please enter the name of the Student - "))
    sid = int(input("Please Enter SID of Student - "))

    if sid<0:
        #Displaying Warning for negative inputs
        print("\nSID can't be negative\n")
    else:
        #inserting sid and name as key value pair in dictionary
        dict1.update({sid: name})
        #inserting name and sid as key value pair in dictionary
        dict2.update({name:sid})
        #asking for the decision to insert new values
        while True :
            isrep = str(input("Either press Y to continue or N to terminate : "))
            #checking for invalid input
            if (isrep not in ['Y', 'N', 'y', 'n']):
                print("\nPlease enter valid input ['Y' or 'N'] ")
                continue
            else :
                break
        if isrep == "N" or isrep == "n":
            break

#printing the dictionary
print("\nQues.6(a) The Dictionary containing {'SID':'Name'} is : %s " % (dict1))

#sorting according to name
ls1=sorted(dict2)
dict3={}
for char in ls1:
    dict3.update({dict2.get(char):char})
print("\nQues.6(b) The Dictionary after sorting according to name : %s" % (dict3))

#sorting according to SID
sort_dic = sorted(dict1)
dict4 = {}
for alph in sort_dic:
    dict4.update({alph: dict1.get(alph)})
print("\nQues.6(c) The Dictionary after sorting according to SID : %s" % (dict4))

print("\nQues.6(d)")
# Taking input SID to be searched
enter_sid = int(input("Enter SID to get name of student : "))
# Searching for sid as key in dic
output_name = str(dict1.get(enter_sid))
# printing name with key sid
print(f"Name of student with SID {enter_sid} is {output_name}.")

#Que7'Code
print("Que7 - Output\n")

num = int(input("Total elements of Fibonacci sequence that you want(must be greater than 1)- "))

#using the formula of the sum of previous two terms is equal to the present term.
n1,n2,n = 1,0,0

#initializing sum with first two terms
sum= n1 + n2

#printing the initial two terms as the recursion is not valid on them
print(f"Fibonnaci sequence with {num} terms")
print(n2,n1,end = " ")

#printing the remaining fibonnaci terms
while n<num-2:
    n0 = n2 + n1
    n2 = n1
    n1 = n0
    print(n0,end = " ")
    n += 1
    sum += n0
average = sum / num
#printing the program end prompt
print(f"\nAverage of total {num} terms of sequence is {average}")
print("end")

#Que8'Code
print ("Que8 - Output\n")
#Given Sets
set1,set2,set3 = {1, 2, 3, 4, 5},{2, 4, 6, 8},{1, 5, 9, 13, 17}

#printing the given sets
print(f"Set1= {set1}\nSet2= {set2}\nSet3= {set3}")

#Que8(a)'Code
symdif = set1.symmetric_difference(set2)
print("\nQues.8(a) Set of all 'elements that are in Set1 and Set2 but not both' is : %s" % (symdif))

#Que8(b)'Code
#set1 union set2
set_u1=set1.union(set2)

#set1 Union set2 Union set3
set_uf=set_u1.union(set3)

#set1 intersection set2
set_i1=set1.intersection(set2)

#set1 intersection set2 intersection set3
set_if=set_i1.intersection(set3)

#set1 intersection set2
set_12=set1.intersection(set2)

#set2 intersection set3
set_23=set2.intersection(set3)

#set3 intersection set1
set_13=set1.intersection(set3)

#final required set
set_f1=set_uf-set_12-set_23-set_13
print("\nQues.8(b) A new set of all elements that are 'in only one of the three sets Set1,Set2 and Set3' is : %s" % (set_f1))

#Que8(c)'Code
set_c1=set_12.union(set_23)
set_c2=set_c1.union(set_13)
set_final=set_c2-set_if
print("\nQues.8(c) A new set of elements that are 'exactly in two of the sets Set1, Set2 and Set3' is : %s" % (set_final))

#Que8(d)'Code
#forming a set containing values from 1 to 10
set_d={1,2,3}
set_d.clear()
for i in range(1,11):
    set_d.add(i)
set_new=set_d-set1
#printing final set
print("\nQues.8(d) A new set of all Integers in the 'range 1 to 10' that are 'not in Set1' is : %s " % (set_new))

#Que8(e)'Code
set_e=set_d-set_uf
print("\nQues.8(e) A new set of all Integers in the range 1 to 10 that are not in Set1,Set2 and Set3 : %s" % (set_e))