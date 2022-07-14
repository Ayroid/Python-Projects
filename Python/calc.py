expression=input("Enter your equation: ")
operators=['+','-','*','/','^']
flg=0
for i in expression:
    if i in operators:
        indx=expression.index(i)
        num1=int(expression[:indx])
        num2=int(expression[indx+1:])
        op=expression[indx]
        flg=1
        break
if flg==1:
    print("Output: ",end='')
    if op=='+':
        print(num1+num2)
    elif op=='-':
        print(num1-num2)
    elif op=='*':
        print(num1*num2)
    elif op=='/':
        print(num1/num2)
    elif op=='^':
        print(num1**num2)
else:
    print("Operator not Recognised")