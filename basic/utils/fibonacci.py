def fib(num):
    if num == 1 or num == 2:
        return 1
    else:
        return fib(num - 1) + fib(num - 2)
        

def app_fibonacci():
    num = int(input('Ingresa número: '))
    fib_1 = fib(num)
    print('El numero de fib de', num, 'es:', fib_1)

app_fibonacci()