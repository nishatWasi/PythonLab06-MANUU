# Roll no: 15
while 1:
    user_in = input("Enter any number to find the factorial :")
    try:
        user_in = int(user_in)
        user_in_len = len(str(user_in))
        tempVal = user_in
        factorial = 1
        for i in range(user_in_len):
            factorial = factorial*(tempVal%10)
            tempVal = int(tempVal/10)
        print("Factorial of ",user_in," is ",factorial)
        break
    except ValueError:
        print("Enter number only.")
        continue
