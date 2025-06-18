#Question 1
list1=["Hey","Dasuya","Hi","Hosharipur",]
result=[i for i in list1 if len(i)<=4]
print("String with less than fout lettors:",result)

print("_ _ _ _ _ _ _ _")
print("_ _ _ _ _ _ _ _")

#Question 2

list1=[i for i in range(20)]
print(list1)
list2=["even" if i%2==0 else "odd" for i in list1]
print("New list: ",list2)

print("_ _ _ _ _ _ _")
print("_ _ _ _ _ _ _")

#Question 3

list1=[i for i in range(1,1000) if i%7==0]
print("Number divisible by 7:",list1)

print("_ _ _ _ _ _ _")
print("_ _ _ _ _ _ _")

#Question 4

str1="Hello everyone ! What are you doning.?"
count=0
for i in str1:
    if i==" ":
        count+=1
        print("Total number of spaces: ",count)

print("_ _ _ _ _ _ _")
print("_ _ _ _ _ _ _")

# Question 5        

list_a=[1,2,3,4]
list_b=[2,3,4,5]
list=[i for i in list_a for j in list_b if i==j]
print("New list:",list)



      

