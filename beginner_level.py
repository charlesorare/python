#1. Basic Syntax and Concepts
#Variables store data like in the case below:-
x=10
print(x)
#When naming variables, pay close attention to the following:names can only start with a letter or an underscore and not
# a number;name characters can only have letters(a-z,A-Z), numbers(1-9) and underscores(_);names are case-sensitive;names
#cannot be of those python reserved keywords like if, else etc.

#Data Types-They include integers, floats, boolean etc

#Operators-Like the case above (=) is an operator.Basically,used for calculations and logic.

#Conditional statements:-
#i)If/else-used for decision-making
age = int(input("Enter your age: "))

if age >= 18:
    print("adult")
else:
    print("minor")
#ii)Loops(for, while)-they repeat actions multiple times.
for i in range(5):
    print(i)

#2. Functions and Modules