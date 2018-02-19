numDays = int(input("Enter the number of days: "))
startDay = int(input("Enter the starting day: "))

def print_month_calendar(numDays, startDay):
    weekday = startDay
    print("Mon   Tue   Wed   Thr   Fri   Sat   Sun")
    for i in range(1, numDays+1):
        if (i >= 10 and weekday <= 7):
            print((startDay - 1) * "  ", i, "  ", end='')
            weekday += 1
        elif(i >= 10 and weekday > 7):
            print("\n", i, "  ",end = '')
            weekday = 2
        elif (weekday <= 7):
            print((startDay - 1) * "      ", i, "   ", end='')
            weekday += 1
        else:
            print("\n", i, "   ", end='')
            weekday = 2
        startDay = 1

    return (weekday-1)
print_month_calendar(numDays, startDay)
