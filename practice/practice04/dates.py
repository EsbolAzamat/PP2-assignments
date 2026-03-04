import datetime
# Task 1

today = datetime.date.today()
diff = today - datetime.timedelta(days=5)
print(diff)


# Task 2 

tomorrow  = today + datetime.timedelta(days=1)
yesterday  = today - datetime.timedelta(days=1)    
print(yesterday, today, tomorrow)

# Task 3

now  = datetime.datetime.now()
clean = now.replace(microsecond=0)
print(clean)

# Task 4

date1 = datetime.datetime(2026, 5, 7)
date2 = datetime.datetime(2026, 5, 1)
diff = date1 - date2
print(diff.total_seconds())