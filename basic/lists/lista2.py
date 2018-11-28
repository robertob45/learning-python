
list = []
def list_(times):
    for x in range(times):
        number = int(input('Ingrese numero(s) a incluir '))
        list.append(number)
    return list

times = int(input('Cantidad de elementos?: '))
list = list_(times)
print(list)
        