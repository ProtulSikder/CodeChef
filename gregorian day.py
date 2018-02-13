import datetime
for _ in range(int(input())):
    year = int(input())
    
    day = datetime.date(year,1,1)

    wkday = day.weekday()

    if wkday == 0:
        print('monday')
    elif wkday == 1:
        print('tuesday')
    elif wkday == 2:
        print('wednesday')
    elif wkday == 3:
        print('thursday')
    elif wkday == 4:
        print('friday')
    elif wkday == 5:
        print('saturday')
    elif wkday == 6:
        print('sunday')
