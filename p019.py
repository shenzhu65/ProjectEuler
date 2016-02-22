import calendar

weekday,ans=0,0
for year in range(1900,2001):
    for month in range(12):
        if month+1!=2:
            if month+1 in [1,3,5,7,8,10,12]:
                days = 31
            else:
                days = 30
        elif calendar.isleap(year):
            days=29
        else:
            days=28
        weekday = (weekday+days)%7
        if weekday==6 and year>1900:
            ans+=1
print(ans)
