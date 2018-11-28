def division(num_1, num_2):
    if num_2 == 0:
        print('El segundo numero no debe ser cero, intenta de nuevo')
    else:
        division_total = num_1 / num_2
        print('El resultado es:',division_total)
        return division_total

def app_division():
    in_1 = int(input('Ingresa numero = '))
    in_2 = int(input('Entre = '))
    division(in_1, in_2)

#app_division()
