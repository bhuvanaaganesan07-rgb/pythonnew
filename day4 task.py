a=int(input("first no: "))
op=input("operation(+,-,*,/):")
b=int(input("second no: "))
if op=='+':
    print("Result:",a+b)
elif op=='-':
    print("Result:",a-b)
elif op=='*':
    print("Result:",a*b)
elif op=='/':
    if b==0:
        print("cannot divisible")
    else:
        print("Result:",a/b)
else:
    print("invalid operation")