ans = True
while ans:
    print("Select the operator")
    print("1. Multiplication")
    print("2. Substraction")
    print("3. Division")
    print("4. exit")

    choice = input("Select the operator number:")

    if choice == '1':
        num1 = float(input("Enter First Number: "))
        num2 = float(input("Enter Second Number:"))
        print(num1,"x",num2, "=", num1*num2)
    elif choice == '2':
        num1 = float(input("Enter First Number: "))
        num2 = float(input("Enter Second Number:"))
        print(num1,"-",num2,"=",num1-num2)
    elif choice == '3':
        num1 = float(input("Enter First Number: "))
        num2 = float(input("Enter Second Number:"))
        print(num1,"/",num2,"=",num1 / num2)
    else:
        exit()

    



