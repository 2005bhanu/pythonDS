#Question 1

t1=(20,55,"Hello",6,78,20,55,"Hello",34)
print(t1)
t1=set(t1)
t1=tuple(t1)
print("After removing duplicate elements: ",t1)

print("-------------------")

#Question 2

l1=[[1,2],[3,4],[5,6]]
print("Original List: ",l1)
l2=[j for i in l1 for j in i]
print("Flattened list: ",l2)

print("----------------")

t=(3,5,1,8,2)
print("Original Tuple: ",t)
t=list(t)
t.sort()
print("Min= ",t[0])
print("Max= ",t[-1])

print("------------------")

#Question 4

l1=[(i,i**3) for i in range(1,6)]
print("List: ",l1)