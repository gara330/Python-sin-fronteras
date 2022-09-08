def preguntarNombre():
    nombre = input('Cual es tu nombre? \n')
    return nombre

def preguntarApellido():
    apellido = input('Cual es tu apellido? \n')
    return apellido

def nombreCompleto(nombre, apellido):
    nCompleto = nombre + " " + apellido
    print(nCompleto + " Bienvenido")
    pass

def main():
    nombre = preguntarNombre()
    apellido = preguntarApellido()
    nombreCompleto(nombre, apellido)
    pass

main()