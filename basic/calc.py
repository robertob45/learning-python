from operations.suma import app_suma
from operations.resta import app_resta
from operations.multiplicacion import app_multip
from operations.division import app_division
from utils.factorial import app_factorial
from utils.fibonacci import app_fibonacci
from conditions.igual import app_verif_igual
from conditions.mayor import app_mayor

print('')
print('Calculadora')
print('')

def calc():
    operation = input("Operacion? (Para salir usa: 'salir'): ")
    print('')

    if operation == '+' or operation == 'suma':
        print('Suma: ')
        app_suma()
        print('')
        calc()
    elif operation == '-' or operation == 'resta':
        print('Resta: ')
        app_resta()
        print('')
        calc()
    elif operation == '*' or operation == 'multiplicacion':
        print('Multiplicacion: ')
        app_multip()
        print('')
        calc()
    elif operation == '/' or operation == 'division':
        print('Division: ')
        app_division()
        print('')
        calc()
    elif operation == 'mayor':
        print('Cual es mayor:')
        app_mayor()
        print('')
        calc()
    elif operation == 'igual':
        print('Iguales?:')
        app_verif_igual()
        print('')
        calc()
    elif operation == 'fibonacci':
        print('Numero fibonacci:')
        app_fibonacci()
        print('')
        calc()
    elif operation == 'factorial' or operation == '!':
        print('Factorial:')
        app_factorial()
        print('')
        calc()
    elif operation == 'salir':
        print('Saliendo...')
    else:
        print('No ingresaste ningun simbolo o palabra valido, intenta de nuevo')
        calc()

#Iniciar programa
calc()
