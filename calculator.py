while True:
    
    print("Enter the first number")
    first_num=int(input())
    print("Enter the second number")
    second_num=int(input())
    print("What is the operator +,-,*,/")
    print("use % to find remainder")
    operator=input()
    #addition
    if operator=='+':
        sum=first_num+second_num
        print(f"The sum of the numbers is {sum}")
    #subtraction
    elif operator=='-':
        result=first_num-second_num
        print(f"The subtraction is {result}")
    #divison
    elif operator=='/':
        result=first_num/second_num
        print(f"The quotient is {result}")
    #multiplication
    elif operator=='*':
        result=first_num*second_num
        print(f"The product is {result}")
    #remainder finder
    elif operator=='%':
        result=first_num%second_num
        print(result)
