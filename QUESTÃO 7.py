import datetime

x = datetime.date.today()
print('Data atual:', x)
y = datetime.timedelta(days= 8)
a = x - y
print('Menos 8 dias:', a)
