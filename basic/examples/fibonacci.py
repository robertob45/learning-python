num = int(input('Ingrese número: '))

fib = 0
fib_2 = 1

while fib_2 < num:
    #fib = fib_2
    #fib_2 = fib + fib_2
    fib, fib_2 = fib_2, fib + fib_2

print('El numero de fibonacci de', num, 'es:', fib)
