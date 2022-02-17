from datetime import datetime
from datetime import timedelta

x = '2021-03-23-20.07.50'
y = datetime.strptime(x, '%Y-%m-%d-%H.%M.%S')
print(y)
