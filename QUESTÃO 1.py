import time
from datetime import timedelta

# A
print(time.gmtime(0))

# B
segundo = time.time()
print('Segundos que se passaram desde a época:', segundo)

# C
print('Momento atual:', time.asctime())

# D
a = time.localtime()
print(a[3:6])

# E
y = timedelta(hours=-3)
print('Fuso horario UTC:', y)
