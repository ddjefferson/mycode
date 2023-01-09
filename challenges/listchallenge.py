#!/usr/bin/env python3 

# add list to code 

wordbank = ["indentation", "spaces"] 

# list of tlg students
tlgstudents= ['Albert', 'Anthony', 'Brenden', 'Craig', 'Deja', 'Elihu', 'Eric', 'Giovanni', 'James', 'Joshua', 'Maria', 'Mohamed', 'PJ', 'Philip', 'Sagan', 'Suchit', 'Meka', 'Trey', 'Winton', 'Xiuxiang', 'Yaping'] 

# print list for readability
print(tlgstudents)

# append the integer <4> to the list wordbank
wordbank.append(4) 
print(wordbank)

# Include an input asking for a number between 0 and 20. Save this as the variable num
num = input("Pick a student number!") 

# Remember that input() always returns a string... convert num into an integer!
num = int(input("Pick a student number!")) 

# 
choice= int(input("Pick a student number!")) 
student_name= tlgstudents[choice] 


print(f"{student_name}  always uses {wordbank[0]} {wordbank[1]} to indent.")) 
