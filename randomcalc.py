import random
sam=random.randint(0,8935893)
print("the first number is",sam)
gam=random.randint(0,98543)
print("the second number is",gam)
#randomizing operators
lst=['+','*','/','-']
choice=random.choice(lst)
#addition
if choice=='+':
    result=sam+gam
    print("the addition is",result)
#multiplication
elif choice=='*':
    result=sam*gam
    print("the multiplication is",result)
#divison
elif choice=='/':
    result=sam/gam
    print("the divison is",result)
#subtraction
elif choice=='-':
    result=sam-gam
    print("the subtraction is",result)
