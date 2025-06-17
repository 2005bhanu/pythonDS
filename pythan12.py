name=input("enter the name:")
student_class=input("enter the class:")
sectin=input("enter the section:")
print("enter marks for 5 subjects:")
marks =[]
for i in(1,6):
    mark =float(input(f"subject (i) marks:"))
    marks.append(mark)
    total_marks = sum(marks)
    percentage =total_marks/5
    print("\n student result")
    print(f"name:{name}")
    print(f"class:{student_class}")
    print(f"section:{section}")
    print(f"percentage:{percentage:2f}%")

x=int(input('enter x'))
y=int(input('enter y'))
z=int(input('enter z'))
print('The value of x is',x)
print('The value of y is',y)
print('The value of z is',z)
print(x+y+z) 

num=int(input('enter a number'))
sqr=num*num
print(sqr)




