def mayor(num_1, num_2):
    if num_1 > num_2:
        print(num_1,'es el numero mas grande.')
    else:
        print(num_2,'es el numero mas grande.')

def app_mayor():
    in_1 = int(input('Ingrese numero 1 = '))
    in_2 = int(input('Ingrese numero 2 = '))
    mayor(in_1, in_2)
