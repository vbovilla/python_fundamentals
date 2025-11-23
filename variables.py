# x = 1;
# y = "Vishnu"
# print(x)
# print(y);

# Variables do not need to declared with any particular type, and can even change type after they have been set.

# x = 4   # x is of type int
# print(x)
# x = "Vishnu";   # x is now of type string
# print(x)

# Casting
x = str(3); # x will be '3'
y = int(3); # y will be 3
z = float(3); # z will be 3.0

print(x)
print(y)
print(z)

a = '3';
print(x + a)

print(type(x))
print(type(y))
print(type(z))
print(type(x+a))


# String variables can be declared either by using single or double quotes:
x = "Vishnu"
# is same as 
x = 'Vishnu'
print(x == x)
print(y == z)

#Vairable names are case-sensitive

a = 4;
A = "Sally"
#A will not overwrite a
print(A)
print(a)


#Multi word variable names

# Camel Case
myVariableName = "John"

# Pascal Case
MyVariableName = "Vishnu"

# Snake Case
my_variable_name = "Harini"


# Manay Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"

print('\n',x,'\n',y,'\n',z)

x = y = z = "Ram"
print(x)
print(y)
print(z)

fruits = ['Banana',"Mango",'Cherry']
x = y = z = fruits
print(fruits)
print(x)
print(y)
print(z)

print("Hello"+"World")
print("Hello","World")