#Question 1
str1=input("Enter a string: ")
l=len(str1)
if 1<2:
 print("Invalid String")
else:
 str1=str2[:2]+str1[1-2:1]
 print("New String- ",str2)

 print("----------------")

 #Question 2
 str1=int(input("Enter the First String- "))
 str1=int(input("Enter the Second String")) 
 a=str1[:1]
 b=str2[:2]
 str1=str1.replace(a,b)
 str=str2.repalce(b,a)
 print("New String= "," "str2)

 print("--------------")

 #Question 3

 str1=int(input("Enter a string: "))
 l=len(str1)
if 1<3:
 print("New String- ",str1)
 elif str1.endswith("ing"):
print("New String- ",str1+"ly")
else:
print("New String- ",str1+"ing")

print("-------------")

#Question 4

str1=input("Enter a string")
if len(str1)==0:
 print("String is empty")
else:
 a=int(input("Enter the index: "))
 if a>len(str1):
  print("Entrt the index is greator than the length of string")
 else:
  print("string= ",str1)
  print("New String= ",str1[:a]+str1[a+1:])