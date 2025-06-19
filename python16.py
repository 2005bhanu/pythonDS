# Question 1

numbers=[1,2,3,4,5,6,7,8,9,10]
print(numbers)

print("_ _ _ _ _ ")

#Question 2

list1=[1,10,100,3,6,8]
print(list1)
print("length= ",len(list1))
list1.insert(59,3)
list1.append(5)
print("New list= ",list1)
print("New length= ",len(list1))

print("_ _ _ _ _ _")

#Question 3

l1=[1,4,2,42,4,6,2,56,4,56,2]
print(l1[::2])

print("_ _ _ _ _ _")

#Question 4

l1=["Gaurav",12,23,33.33,"Sharma",True]
l2=[]
for i in l1:
    if type(i)==str:
        l2.append(i)
        print("New list= ",l2)

print("_ _ _ _ _ _")

#Question 5

l1=["Gaurav",12,23,33.33,"Sharma",True]
sum=0
for i in l1:
    if type(i)==int:
        sum==sum+i
        print("sum of all numbers= ",sum)

print("_ _ _ _ _ _ _ ")

#Question 6

l1=["Diya","Pihu","Navjot","Neha","Palak"]
print(l1)
frnd1=input("Enter a friend:")
l1.append(frnd1)
print(l1)
frnd2=input("Enter the most important frind: ")
ind=input("Enter the location: ")
l1.insert(ind,frnd2)
print("New list: ",l1)