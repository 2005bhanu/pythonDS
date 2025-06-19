#Question 1

um=int(input("Enter a number: "))
if num==1:
    print("January")
elif num==2:
    print("February")
elif num==3:
    print("March")
elif num==4:
    print("April")
elif num==5:
    print("May")
elif num==6:
    print("June")
elif num==7:
    print("July")
elif num==8:
    print("August")
elif num==9:
    print("September")
elif num==10:
    print("October")
elif num==11:
    print("November")
elif num==12:
    print("December")
else:
    print("Invalid")

    print("---------------")

#Question 2


a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
fname=input("Enter your first name: ")
lname=input("Enter your last name: ")
name=fname+ " "+lname
print("a= ",a)
print("b= ",b)
print("name= ",name)
if a>b:
    print(a, " is greater than ",a)
    for i in range(5):
        print(fname)
elif b>a:
    print(b," is greater than ",a)
    for i in range(3):
        print(lname)
else:
    print(a," is equal to ",b)


print("------------------------")
#Question 3

str1=input("Enter first string: ")
str2=input("Enter second string: ")
if str1==str2:
    print("String 1 is equal to string 2")
else: 
    print("Strings are not equal")
if str1 is str2:
    print("String 1 and String 2 are equal(ID)")
else:
    print("Strings are not equal(ID)")


print("-----------------")

#Question 4

str1=input("Enter first string: ")
str2=input("Enter second string: ")
# Strings can't be converted into numbers
if str1 is str2:
    print("String 1 and String 2 are equal")
else:
    print("Strings are not equal(ID)")


print("--------------------")
      #Question 5
      
num=int(input("Enter a number: "))
sum=0
for i in range(num+1):
    sum=sum+i
print("Sum from 0 to ",num,"= ",sum)


print("--------------------------------")

#Question 6

num=int(input("Enter a number: "))
print("Even numbers are ")
for i in range(num+1):
    if i%2==0:
        print(i,end=" ")


print("-----------------------------")

#Question 7

num=int(input("Enter a number: "))
op=input("Enter the operator (+ or -): ")
if op=='+':
    for i in range(num):
        print(i,end=" ")
elif op=="-":
    for i in range(num,0,-1):
        print(i,end=" ")
else:
    print("Wrong operator")


print("---------------------")

# Question 8

num=int(input("Enter a number: "))
for i in range(1,11):
    print(num," x ",i," = ",num*i)


print("----------------------------")

#Question 9

for i in range(1,5):
    for j in range(1,i+1):
        print(j,end=" ")
    print()


print("------------------------")

#Question 10

n=int(input("Enter a number: "))
print("Squares of ",n," natural numbers: ")
for i in range(1,n+1):
    print(i*i,end=" ")