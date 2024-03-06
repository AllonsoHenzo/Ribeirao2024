t1 = int(0)
t2 = int(1)
t3 = int(0)
valor = int(input('Digite um número: '))

while valor > t3:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
if valor == 0 or valor == 1:
    print ('Este número faz parte da sequência de Fibonacci.')
elif valor == t3:
    print ('Este número faz parte da sequência de Fibonacci.')
else:
    print ('Este número não faz parte da sequência de Fibonacci.')
