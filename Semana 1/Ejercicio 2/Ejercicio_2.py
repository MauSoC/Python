###	2.	Crear un programa que solicite al usuario una cadena de caracteres y luego imprima la cadena al revés.

def CadenaRe(cadena):
    #utilizamos la sintaxis [::-1] para invertir la cadena y la retornamos directamente con ayuda del fstring
    return f'{cadena[::-1]}'

if __name__ == "__main__":
    #Pedimos la cadena al usuario
    cadena = input('Ingresa una cadena: ')
    #llamamos la funcion y mandamos la cadena para imprimir el resultado
    print(CadenaRe(cadena))
    
    