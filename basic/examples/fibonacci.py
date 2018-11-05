fin = int(input('Fin de la sucesión: '))

fib = 0
fib_2 = 1
while fib_2 < fin:
    fib, fib_2 = fib_2, fib + fib_2
    print(fib)
