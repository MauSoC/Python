###	1.	Crear un programa que solicite al usuario su nombre 
### y su edad, y luego imprima un mensaje de bienvenida con esa información..

def saludo (nombre=None, edad=None):
    return f'Hola {nombre}, gracias por unirte al programa tu edad es: {edad}.'


if __name__ == "__main__":
    nombre = input('Ingresa tu nombre: ')
    edad = int(input('ingresa tu edad: '))
    print(saludo(nombre, edad))
