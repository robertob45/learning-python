list_2 = []

def while_(i):
    while i % 2 == 1:
        i = int(input('Ingrese numero: '))
        list_2.append(i)
    return list_2

i = int(input('Ingrese numero: '))
i = while_(i)
print(list_2)
