def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return factorial(num - 1) * num
    # 1 4 6 24 120 720

def app_factorial():
    num = None
    while num == None:
        try:
            num = int(input('Ingresa numero: '))
        except ValueError:
            print('Numero invalido, intenta de nuevo')

    fact = factorial(num)
    print(fact)

# def app_factorial():
#     num = int(input('Ingresa numero: '))
#     fact = factorial(num)
#     print(fact)

# def factorial(num):
#     fact = 1
#     while num > 1:
#         fact = num * fact
#         num = num - 1
#     return fact

