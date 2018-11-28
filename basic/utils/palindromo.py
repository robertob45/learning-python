def palindromo(string):
    string_2 = string.lower()
    string_2 = string.replace(' ', '')

    if string_2 == string_2[::-1] :
        print('Esta frase es un palindromo')
    else:
        print('Esta frase no es un palindromo')
    return string_2

string = input('Frase?: ')
string_2 = palindromo(string)
