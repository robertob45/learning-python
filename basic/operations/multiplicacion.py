def multip(num_1, num_2):
    print('Multiplicando:', num_1, '*', num_2)
    multip_total = num_1 * num_2
    print('El resultado es:',multip_total)
    return multip_total

def app_multip():
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
    multip(inp_1, inp_2)

#app_multip()
