import datetime
currenttime=datetime.datetime.now().strftime("%d/%m/%Y----%H:%M:%S")
print currenttime

from datetime import datetime

start_date = '11/12/2018 16:05:15'
end_date = '12/12/2018 23:55:20'
#end_date = 'Sun Sep 16 16:05:15 +0000 2012'

def __datetime(date_str):
    return datetime.strptime(date_str, '%d/%m/%Y %H:%M:%S')

start = __datetime(start_date)
end = __datetime(end_date)

delta = end - start
print delta  # prints: 1 day, 7:50:05
print delta.total_seconds()
