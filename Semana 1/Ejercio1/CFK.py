#	1.	Crea un script que permita a los usuarios convertir unidades de temperatura entre Celsius, Fahrenheit y Kelvin.
def Celsius(opt, temUser):
    if opt == 1:
        return f'Los grados Celsius {temUser} a Fahrenheit son: {((temUser*1.8)+32)}'
    else:
        return f'Los grados Celsius {temUser} a Kelvin son: {temUser+273.15}'

def Fahrenheit(opt, temUser):
    if opt == 3:
        return f'Los grados Fahrenheit {temUser} a Celsius son: {(temUser-32)*(5/9)}'
    else:
        return f'Los grados Fahrenheit {temUser} a Kelvin son: {((temUser-32)/1.8)+273.15}'
        
      
        
def Kelvin(opt, temUser):
    if opt == 5:
        return f'Los grados Kelvin {temUser} a Celsius son: {temUser-273.15}'
    else:
        return f'Los grados Kelvin {temUser} a Fahrenheit son: {1.8*(temUser-273)+32}'



def convertir(temUser=None):
    print(''' Menu:
    1.- Celsius -> Fahrenheit
    2.- Celsius -> Kelvin
    3.- Fahrenheit -> Celsius
    4.- Fahrenheit -> Kelvin
    5.- Kelvin -> Celsius
    4.- Kelvin -> Fahrenheit\n\n''')
    opt = int(input('Seleccione en que unidad desea convertir la temperatura '))
    if opt == 1 or opt == 2:
        return Celsius(opt,temUser)
    elif opt ==3 or opt == 4:
        return Fahrenheit(opt,temUser)
    elif opt == 5 or opt == 6:
        return Kelvin(opt,temUser)
    else:
        return f'La opcion {opt} NO ES VALIDA'



def main():
    temUser = float(input('Ingrese una temperatura: '))
    print(convertir(temUser))



if __name__ == "__main__":
    main()