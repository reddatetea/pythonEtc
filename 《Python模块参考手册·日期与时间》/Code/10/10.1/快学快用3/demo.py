from  datetime import datetime, date

now_dt = datetime.today()
before_dt = now_dt.replace(year = 2015, day =  23)
timedelta_01 = now_dt - before_dt

da_01 = date.today()
da_02 = da_01.replace(day = 25, year = 2512)
timedelta_02 = da_02 - da_01
print(f"timedelta_01 = {timedelta_01}, \ntimedelta_02 = {timedelta_02}")
