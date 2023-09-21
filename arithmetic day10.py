# Create a program that reads two integers, a and b, from the user. Your program should
# compute and display:
# • The sum of a and b
# • The difference when b is subtracted from a
# • The product of a and b
# 6 1 Introduction to Programming Exercises
# • The quotient when a is divided by b
# • The remainder when a is divided by b
# • The result of log10 a
# • The result of a^b
# 
a=int(input("Plese enter an integer: "))
b=int(input("Plese enter another integer: "))
print("the sum of",a ,"and",b ,"is: ", a+b)
print("the difference between",a ,"and",b ,"is: ", a-b)
print("the product of",a ,"and",b ,"is: ", a*b)
print("the quotient of",a ,"and",b ,"is: ", a/b)
print("the remainder when ",a ,"is divided by",b ,"is: ", a%b)
print("the sum of",a ,"and",b ,"is: ", a+b)
import math   

print("Log value of a is : ", math.log(a))
print("The result of a^b is: ", a**b)
