num = int(input('Ingrese número: '))

fib = 0
fib_2 = 1
print('La sucesión de fibonacci de', num, 'es:')
while fib_2 < num:
    fib, fib_2 = fib_2, fib + fib_2
    print(fib)
