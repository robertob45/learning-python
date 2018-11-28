p1 = {}
p2 = {}
p3 = {}
p4 = {}
p5 = {}

people = []

x = 1

while x < 3:
    name = input('Ingresa nombre: ')
    l_name = input('Ingresa apellido: ')
    age = int(input('Ingresa edad: '))
    people.append(name)
    people.append(l_name)
    people.append(age)
    print('')
    if x == 1:
        p1["name"] = name
        p1["l_name"] = l_name
        p1["age"] = age
    elif x == 2:
        p2["name"] = name
        p2["l_name"] = l_name
        p2["age"] = age
    elif x == 3:
        p3["name"] = name
        p3["l_name"] = l_name
        p3["age"] = age
    elif x == 4:
        p4["name"] = name
        p4["l_name"] = l_name
        p4["age"] = age
    elif x == 5:
        p5["name"] = name
        p5["l_name"] = l_name
        p5["age"] = age
    x = x + 1

print(people)
print(p1)
print(p2)
print(p3)
print(p4)
print(p5)
