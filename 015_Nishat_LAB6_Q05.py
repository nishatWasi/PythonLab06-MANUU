# Roll no: 15
while 1:
    year = input("Enter a year to check leap year :")
    try:
        year = int(year)
        if year%4 == 0 or year%100 == 0 or year%400 == 0:
            print(year," is a leap year")
        else:
            print(year," is not a leap year")
        break
    except ValueError:
        print("Enter year in number only.")
        continue
