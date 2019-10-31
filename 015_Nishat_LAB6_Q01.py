#Name :       Mohd. Nishat Wasi
#Roll no.:    18BTCS015HY
#Enrl no.:    A180492
while 1:
    user_in1 = input("Enter a number :")
    user_in2 = input("Enter another number :")
    try :
        in1 = int(user_in1)
        in2 = int(user_in2)
        print("Press 'A' to addition\nPress 'S' to subtraction\nPress 'M' to multiply\nPress 'D' to divide.")
        select = input("Press here :)")
        if select == 'a' or select == 'A':
            print(in1+in2)
        elif select == 's' or select == 'S':
            if in1>in2:
                print(in1-in2)
            else:
                print(in2-in1)
        elif select == 'm' or select == 'M':
            print(in1*in2)
        elif select == 'd' or select == 'D':
            if in1>in2:
                print(in1/in2)
            else:
                print(in2/in1)
        else:
            print("Press valid key in upper or lower.")
        break
    except ValueError:
        print("Enter number only.")
        continue
