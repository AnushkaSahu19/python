# python program to copy a list
'''li=[]
n=int(input("enter size of list"))
for i in range(0,n):
    j=int(input("enter elements of list"))
    li.append(j)
print("original list",li)
list_copy=li.copy()
print("after cloning",list_copy)  '''

# python program to count occurrence of elements in list

'''li=[]
n=int(input("enter size of list"))
for i in range(0,n):
    j=int(input("enter elements of list"))
    li.append(j)
print("original list",li)
p=int(input("enter number to be counted"))
print(p,'has occurred',li.count(p),'times')  '''

#python program to find sum and average of list 

'''li=[]
n=int(input("enter size of list"))
for i in range(0,n):
    j=int(input("enter elements of list"))
    li.append(j)
    sum=0
    for i in li:
         sum=sum+i
    avg=sum/len(li)
    
print("original list",li)
print("sum of elements of list",sum) 
print("average of list ",avg)  '''

#  python program to find sum of elements of list

'''li=[]
n=int(input("enter size of list"))
for i in range(0,n):
    j=int(input("enter element of list"))
    li.append(j)
    sum=0
    for i in li:
        sum=sum+i
print("original list:",li)
print("sum of elements:",sum) '''

# python program to find multiplication of elements:

'''li=[]
n=int(input("enter size of list"))
for i in range(0,n):
    j=int(input("enter elements of list"))
    li.append(j)
    product=1
    for i in li:
        product=product*i
print("original list:",li)
print("product of list elements",product) '''
# python program to find smallest number in python

'''def small(li):
    small=min(li)
    return small

li=[]
n=int(input("enter size of list"))
for i in range(0,n):
    e=int(input("enter elemets of list:"))
    li.append(e)
print("smallest number")
print(small(li))
'''
# pythomn program to find largest number in a list


     
'''l=[]
def holdsell():
    day=(input("enter no of hold sells"))
    for i in (day):
        l.append(int(input("enter sell ammount of each day")))
    print("total sell day wise:",l)
holdsell() '''
'''l=[]
def append_ele():
    while True:
        l.append(input("enter elements for appending"))
        if "y"!=(input("enter y for continue reading")):
            break
        
    print("your elements are ",l)
append_ele()  '''

'''def sum(n):
    if n==1:
        return 1
    else:
        return n+ sum(n-1)
n=int(input("enter a number"))
if n<1:
    print("enter a posituve number")
else:
    print("sum of numbers is:",sum(n)) '''

'''def append_elements():
    elements=[]
    while True:
        value=input("enter a value to append to the list(or type 'no' to finish):")
        if value=='no':
            break
        elements.append(value)
    print("the final list",elements)
append_elements()   '''

'''def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
n=int(input("enter a number"))
if n>0:
    print("factorial of number is :",fact(n))
else:
    print("enter a positive number") '''

"""def get_sales(num_days):
    sales=[]
    for day in range(1,num_days+1):
        s=float(input(f"enter sales for day{day}:"))
        sales.append(s)
    return sales

num_days=5
sales_data=get_sales(num_days)
print(f"sales for each_days:{sales_data}")"""
# simple interest
'''p=int(input("enter principal ammount"))
t=int(input("enter time"))
r=int(input("enter interest rate"))
si=p*(r+t)/100
print("calculated simple interest rate is ",si) '''

# area
'''r=float(input("enter radius"))
a=3.14*r*r
print("area of circle is",a)
b=int(input("enter base of triangle"))
h=int(input("enter height of triangle"))
t=(1/2)*b*h
print("area of triangle is ", t)  '''
 
 # max of 3 no
'''a=int(input("enter a number"))
b=int(input("enter another number"))
c=int(input("enter other number"))
if a>b and a>c:
    print("a is greatest",a)
elif b>a and b>c:
    print("b is greatest",b)
else:
    print("c is greatest",c)  '''

# even or odd

'''a=int(input("enter a number"))
if a%2==0:
    print("it is even")
else:
    print("it is odd")  '''

# leap year

'''y=int(input("enter year")) 
if(y%4==0 or y%100!=0 or y%400==0):
    print("it is a leap year")
else:
    print("it is not a leap year") '''

# table of no

'''x=int(input("enter a number"))
print("table of number is")
for i in range(1,11):
    
    print(x , "*",i,"=",x*i)  '''

# factorial of number

# calculator
'''x=int(input("enter a number"))
y=int(input("enter another number"))
operator=(input("enter operation to be performed")
match operator:
    case "*" :
        value=x*y
        print("multiplication of two num is",value)
    case "+":
        value=x+y
        print("addition of two num is",value)
    case "-":
        value=x-y
        print("substraction of two num is", value)
    case "/":
        value=x/y
        print("division of two num is",value)  '''

'''string="hello world"
char_list=list(string)
char_list[2],char_list[6]=char_list[6],char_list[2]
new_srting="".join(char_list)
print(new_srting) '''

'''def length(li):
    counter=1
    for i in li:
        counter=counter+1
    return counter
li=[1,2,3,4,5,6,7]
print(li)
print("length of list",length(li)) '''
'''def length(li):
    return len(li)
li=[1,2,3,4,5,6,7]
print(li)
print("length of list",length(li))  '''

'''a=int(input("enter a number"))
b=int(input("enter a number"))
if a>b:
    print("a is greatest")
else:
    print("b is greatest",b) '''

def check(list,element):
    for i in list:
        if i==element:
            return True
        else:
            return False
li=[1,3,4,5,6,7]
element=3
print(li)
print("check if",element,"is in",li)
print(check(li,element))
