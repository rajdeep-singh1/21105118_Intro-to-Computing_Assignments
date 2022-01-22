#Que1 Code

print("Output of Question 01")

#defining average function

def avg3():     #Creating a function which takes 3 numbers as input and print's their average
    
    print("Instruction : Don't use , in Values ")
    num1 = int(input("Enter first Number : "))
    num2 = int(input("Enter Second Number : "))
    num3 = int(input("Enter Third Number : "))
    
    avg = (num1 + num2 + num3)/3

    if avg != int(avg): #Making the output presentale!
        avg = round(avg , 2)
    print("Average of given numbers is : " , avg)

#calling the function
avg3()



#Que2 Code

print("Output of Question 02")

#Predefined Variables
rate = 0.20
standard_deduction = 10000
dependent_deduction = 3000

#Values to be inputed by user
print("Instruction : Don't use , in Values ")
gross_income = float(input("Enter your gross income : "))
dependents_numbers = int(input("Enter number of dependents : "))

#Calculating Taxable Income
taxable_income = round(gross_income - standard_deduction - ( dependent_deduction * dependents_numbers),1)

def tax():         #Defining function which calculate and returns tax value
    tax = taxable_income*rate
    if tax < 0:    
        return 0
    else:
        return tax

#calling the function
Tax_Value = tax()

#printing the final tax value
print("Your tax is",Tax_Value,"$")




#Que3 Code

print("Output of Question 3")
#Taking input from the user
SID = int(input("Enter the SID of the Student : "))
name = input("Enter the Name of the Student : ")
gender = input("Enter the gender of the Student\n(Use Gender values: [F] (For Female), [M] (For Male), [U] (For Unknown)) : ")
course_name = input("Enter the course name of the student\n(List of Courses : CSE, ECE, EE, Aero, Prod, Civil, Mech, Metta) : ")
cgpa = round(float(input("Enter the CGPA of the student : ")), 1)
gender = gender.upper()

#Creating the list
Student = [SID, name, gender, course_name, cgpa]

#printing the required list
print(Student)



#Que4 Code

print("Output of Question 04")

#Creating empty list of marks 
Mark = []

#defining a function which takes which takes input from the user and insert it to the list
def Marklist():
    i = 1
    while i<6:
        temp = int(input("Enter Marks of the Student Respective : "))
        Mark.append(temp)
        i+=1
    return(Mark)

#Calling the function
Marklist()

#Sorting Marks
Mark.sort()
print(Mark)

#Que5(a) Code

print("Output of Question 5(a)")

color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color.pop(3)
print("\n",color,"\n")

#Que5(b) Code

print("Output of Question 5(b)")

color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color[3:5]=[] ; color.insert(3,"Purple")
print("\n",color,"\n")

