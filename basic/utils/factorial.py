def factorial(num):
    fact = 1
    while num > 1:
        fact = num * fact
        num = num - 1
    return fact

def app_factorial():
    num = int(input('Ingresa numero: '))
    fact = factorial(num)
    print(fact)
