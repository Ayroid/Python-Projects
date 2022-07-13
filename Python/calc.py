expression=input("Enter your equation: ")
operators=['+','-','*','/']
flg=0
for i in expression:
    if i in operators:
        indx=expression.index(i)
        num1=expression[:indx]
        num2=expression[indx+1:]
        op=expression[indx]
        flg=1
        break
if flg==1:
    print("Output: ",end='')
    if op=='+':
        print(int(num1)+int(num2))
    elif op=='-':
        print(int(num1)-int(num2))
    elif op=='*':
        print(int(num1)*int(num2))
    elif op=='/':
        print(int(num1)/int(num2))