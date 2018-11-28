# Convertimos los valores en numeros con int()
def suma(num_1, num_2):
    suma_total = num_1 + num_2
    print('El resultado es:',suma_total)
    return suma_total

def app_suma():
    in_1 = int(input('Ingresa numero 1: '))
    in_2 = int(input('Ingresa numero 2: '))
    suma(in_1, in_2)

#app_suma()
