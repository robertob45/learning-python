def division(num_1, num_2):
    if num_2 == 0:
        print('El segundo numero no debe ser cero, intenta de nuevo')
    else:
        print('Dividiendo:', num_1, 'entre', num_2)
        division_total = num_1 / num_2
        print('El resultado es:',division_total)
        return division_total

def app_division():
    inp_1 = None  # Can be used 'None' instead of 0 too
    inp_2 = None
    while inp_1 == None:
        try:
            inp_1 = int(input('Numero 1?: '))
        except ValueError:
            print('Numero invalido, intenta de nuevo')
    while inp_2 == None:
        try:
            inp_2 = int(input('Numero 2?: '))
        except ValueError:
            print('Numero invalido, intenta de nuevo')
    division(inp_1, inp_2)

#app_division()
