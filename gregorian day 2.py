import datetime
for _ in range(int(input())):
    wkdays = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    year = int(input())
    print(wkdays[datetime.date(year,1,1).weekday()])
