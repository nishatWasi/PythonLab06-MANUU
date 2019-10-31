#Name :       Mohd. Nishat Wasi
#Roll no.:    18BTCS015HY
#Enrl no.:    A180492
thisList = ['5','3','5','2','7','8','9','1','4','6']
print(thisList," is the given list.")
user_in = input("Enter 'm' to find minimum number or 'M' to find maximum number :")
if user_in == 'm':
    print(min(thisList)," is the minimum number.")
elif user_in == 'M':
    print(max(thisList)," is the maximum number.")
else:
    print("Enter 'm' or 'M' only")
