import math

#1
x=int(input())
if(x%2==0): print("Even")
else: print("Odd")

#2
t=0
for i in range(1, 101):
    t+=i
print(t)

#3
evenNum= list()
for i in range(1, 51):
    if(i%2==0): evenNum.append(i)
for i in evenNum:
    print(i)

#4
a=int(input())
b=int(input())
print(max(a,b))

#5
t=int(input())
for i in range(2,t):
    t*=i
print(t)

#6
val=1
l=list()
for i in range(0, len(l)):
    if(l[i]==val): print(i)
