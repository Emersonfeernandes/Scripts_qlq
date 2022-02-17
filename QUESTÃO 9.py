import datetime

hj = datetime.date.today()
print('Hoje é:', hj)
anton = hj - datetime.timedelta(days=2)
damanha = hj + datetime.timedelta(days=2)

print('Antes de ontem:', anton)
print('Depois de amanhã:', damanha)
print('A diferença de antes de ontem e depois de amanhã', damanha - anton)
