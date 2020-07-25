year = int(input("Enter a year: "))
if year >= 1582:
    if (year % 4) != 0:
        if (year % 400) != 0:
            typeyear = "common year"
        elif (year % 100) !=0:
            typeyear = "Leap year"
        else:
            pass
    else:
        typeyear = "Leap year"
    print("The year you have input is: " + typeyear)
else:
    print("Not within the Gregorian Calendar period")

