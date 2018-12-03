def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
    #1 1 2 3 5 8 13 21
        
def app_fib():
    n = None
    while n == None:
        try:
            n = int(input('Ingresa numero: '))
        except ValueError:
            print('Numero invalido, intenta de nuevo')

    num = fib(n)
    print('El numero fibonacci numero', n, 'es:', num)

# def fibonacci(num):
#     fib = 0
#     fib_2 = 1
#     while fib_2 < num:
#         fib, fib_2 = fib_2, fib + fib_2
#     return fib
