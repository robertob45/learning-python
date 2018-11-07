def factorial(num):
    fact = 1
    while num > 1:
        fact = num * fact
        num = num - 1
    return fact


num = int(input('Ingrese numero: '))
fact = factorial(num)
print(fact)
