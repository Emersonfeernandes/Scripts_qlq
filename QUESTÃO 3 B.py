import time

inicio = time.perf_counter()
def ola():
    print('Olá, mundo!')


def ola1():
    time.sleep(3)
    print('Olá, mundo!')


ola()
ola1()
ola1()
ola1()
ola1()
fim = time.perf_counter()
print('O tempo para execução de todo programa foi de:', fim - inicio)
