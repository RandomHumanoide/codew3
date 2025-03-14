#1
t= 1
while(t<=14):
    print(t)
    t+=1
#2
s= input()
def greeting(name):
    print("Hello", name)
greeting(s)
#3
a,b = list(map(int, input().split()))
def multi(x,y):
    print(x/y)
try:
    multi(a,b)
except b==0:
    print("can't divide by 0")

firstList= ["a","b","c","d"]
for i in firstList:
    print(i)

s= "Math is kind of fun"
for i in s:
    print(i)

firstTuple= (1, 2, 3, 4 ,5)
for i in firstTuple:
    print(i)

firstDic= {
    "name": "Tuna",
    "animal": "Fish",
    "breed": "Yellow Fin",
    "weight": 100
}
for key in firstDic.items():
    print(key)

for i in range(3,14):
    print(i)

for i in range(3,14,3):
    print(i)