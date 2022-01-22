#Code_for_Question_1
print("Output of Question - 1\n")

#taking_string_input_from_the_user
sequence = input("User! Enter the String : ")

print("(a).\tlength of the given String is : ", len(sequence))

#defining_a_function_which_returns_reversed_string
def reverse(a):
    return a[ : :-1]

print("\n(b).\tString in reverse order is : ",reverse(sequence))

sliced = sequence[10:26]

print("\n(c).\tTrimmed Sting would be : ",sliced)

#storing_the_value_of_given_sting_in_an_temporary_variable_to_keep_Original_Unmodified
temp = sequence   
temp = temp.replace("a case sensitive","object oriented")
print("\n(d).\tThe Modified String is : ",temp)

substr = "a"
index = sequence.find(substr)
print("\n(e).\tThe Index of first occurence of the given substring is : ",index)

nospace_str = sequence.replace(" ","")
print("\n(f).\tEntered String with no spaces is : ",nospace_str)


#Code_for_Question_2

#defining_variables_as_required_in_que
name = input("Hey User!,Enter your name : ")
deprt_name = input("Enter your department : ")

#capitalising_department_name
deprt_name = deprt_name.upper()

SID = int(input("Enter your SID : "))
cgpa = float(input("Enter your cgpa : "))

print("Output of Que.2\n")
print("Hey,",name,"Here!","\nMy SID is",SID,"\nI am from",deprt_name,"department and my CGPA is",cgpa)


#Code_for_Question_3
print("Output of Question 3\n")

#defining_given_variables
a = 56
b = 10

print("(a).\t Calculated Value of a & b = ",(a & b))
print("(b).\t Calculated Value of a | b = ",(a | b))
print("(c).\t Calculated Value of a ^ b = ",(a ^ b))
print("(d).\t Calculated Value by Left shifting both a and b with 2 bits : ","a = ",a<<2,"b = ",b<<2)
print("(e).\t Calculated Value by Right shifting a with 2 bits and b with 4 bits : ","a = ",a>>2,"b = ",b>>4)


#Code_for_Question_4
print("Output of Question 4\n")

num1 = float(input("Hey User! Enter First Digit : "))
num2 = float(input("Hey User! Enter Second Digit : "))
num3 = float(input("Hey User! Enter Third Digit : "))

#assuming_num1_as_greatest_integer

greatest_dgt = num1
if num2 > greatest_dgt:
    greatest_dgt = num2     #updating_value_of_greatest_digit
    
    if  num3 > greatest_dgt:
        greatest_dgt = num3     #further_updating_value_of_greatest_digit

print("The greatest digit is ",greatest_dgt)


#Code_for_Question_5
print("Output of Question 5\n")

sequence = input("Enter the String : ")

#defining_a_function_which_takes_two_strings_as_input_&_check_for_one_in_another
def checkstr(a,b):
    if "a" in b:
        print("Yes")
    else:
        print("No")

#Calling_the_funcion
checkstr("name",sequence)


#Code_for_Question_6
print("Output of Question 6\n")

#defining_a_function_which_checks_for_formation_of_triangle

sides = []
for i in range(1,4):
    temp = int(input("Enter the dimension of side = "))
    sides.append(temp)

sides.sort()    #sorting_the_list

#checking for the given condition
if int(sides[2]) < (int(sides[0]) + int(sides[1])):
    print("Yes")
else:
    print("No")

