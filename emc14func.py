def mul():
    a=int(input("A:"))
    b=int(input("B:"))
    print(a*b)
mul()

def findevenorodd(N1):
    if N1%2==0:
        print("even")
    else:
        print("odd")
num=int(input())
findevenorodd(num)

def printrange(a,b):
    for i in range(a,b+1):
        print(i)
x=int(input())
y=int(input())
printrange(x,y)
