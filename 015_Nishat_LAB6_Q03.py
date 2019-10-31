# Roll no: 15
while 1:
    user_in = input("Enter any number to find the sum of its digits :")
    try:
        user_in = int(user_in)
        user_in_len = len(str(user_in))
        tempVal = user_in
        DigitSum = 0
        for i in range(user_in_len):
            DigitSum =DigitSum+(tempVal%10)
            tempVal = int(tempVal/10)
        print("Sum of ",user_in," is ",DigitSum)
        break
    except ValueError:
        print("Enter number only.")
        continue
