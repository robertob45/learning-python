def mayor(num_1, num_2):
    if num_1 > num_2:
        print(num_1,'es el numero mas grande.')
    else:
        print(num_2,'es el numero mas grande.')

def app_mayor():
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
    mayor(inp_1,inp_2)