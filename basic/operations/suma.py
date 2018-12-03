# Convertimos los valores en numeros con int()
def suma(num_1, num_2):
    print('Sumando:',num_1,'+',num_2)
    sum_total = num_1 + num_2
    print('El total es:',sum_total)
    return sum_total

def app_suma():
    inp_1 = None #Can be used 'None' instead of 0 too
    inp_2 = None
    while inp_1 == None:
        try:
            inp_1 = int(input('Numero 1?: '))
        except ValueError:
            print('Numero invalido, intenta de nuevo')
    while inp_2 is None:
        try:
            inp_2 = int(input('Numero 2?: '))
        except ValueError:
            print('Numero invalido, intenta de nuevo')
    suma(inp_1,inp_2)

#######################################################################

# def app_sum():
#     while True:
#         try:
#             in_1 = int(input('Numero 1?: '))
#             in_2 = int(input('Numero 2?: '))
#             break
#         except:
#             print('Numero invalido, intenta de nuevo')
#     sum(in_1,in_2)
# app_sum()

# def app_sum():
#     in_1 = int(input('Numero 1?: '))
#     in_2 = int(input('Numero 2?: '))
#     sum(in_1, in_2)
# app_sum()


#######################################################################

#######################
#  Primer intento :)  #
#######################

# def app_sum():
#     try:
#         inp_1 = int(input('Numero 1?: '))
#     except ValueError:
#         print('Numero invalido, intenta de nuevo')
#         app_sum()
    
#     try:
#         inp_2 = int(input('Numero 2?: '))
#     except ValueError:
#         print('Numero invalido, intenta de nuevo')
#         app_sum()

#     sum(inp_1,inp_2)
    
# app_sum()

#########################################################################   
