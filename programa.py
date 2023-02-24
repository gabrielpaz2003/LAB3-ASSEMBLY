
#Autores: Gabriel Paz y Nelson Garcia
#Curso: Assembly
#Fecha: 22/02/2023

def complemento_a1(binario): #Funcion que calcula el complemento a 1 de un numero binario
    complemento = ''
    for bit in binario:
        complemento += '0' if bit == '1' else '1'
    return complemento

def complemento_a2(binario): #Funcion que calcula el complemento a 2 de un numero binario
    complemento = complemento_a1(binario)
    decimal = int(complemento, 2) + 1
    return bin(decimal)[2:].zfill(8)

print("")
print("-------BIENVENIDO AL PROGRAMA DE OPERACIONES CON BINARIOS Y HEXADECIMALES-----------")
print("1.CALCULAR BINARIOS COMPLEMENTO A1 Y A2")
print("2.CALCULAR HEXADECIMALES")
print("3.SALIR")
print("")
op = int(input("Ingrese una opción: ")) #Menu de opciones

while op != 3:
    if op == 1: #Opcion para calcular complementos
        binario = input("Ingrese un número binario de 8 bits: ")
        complemento_1 = complemento_a1(binario)
        complemento_2 = complemento_a2(binario)

        print(f"Complemento a1: {complemento_1}")
        print(f"Complemento a2: {complemento_2}") 

    if op == 2:  #Opcion para convertir de decimal a hexadecimal y viceversa

        print("1. Convertir de decimal a hexadecimal")
        print("2. Convertir de hexadecimal a decimal")
        opcion = input("Ingrese una opción: ")
        if opcion == "1": #Opcion para convertir de decimal a hexadecimal
            decimal = int(input("Ingrese un número decimal para convertirlo a hexadecimal: "))
            if decimal > 4095: #Validacion para que el numero decimal no sea mayor a 4095
                print("El número debe ser menor o igual a 4095")
                exit()
            else:
                hexadecimal = hex(decimal)[2:].zfill(3)
                print("El número hexadecimal es:", hexadecimal)
        elif opcion == "2": #Opcion para convertir de hexadecimal a decimal
            hexadecimal = input("Ingrese un número en hexadecimal de 3 dígitos: ")
            if len(hexadecimal) > 3:#Validacion para que el numero hexadecimal no sea mayor a 3 digitos
                print("El número debe tener 3 o menos digitos")
            else: 
                decimal= int(hexadecimal, 16)
                print("El número decimal es:", decimal)

    print("")
    print("-------BIENVENIDO AL PROGRAMA DE OPERACIONES CON BINARIOS Y HEXADECIMALES-----------")
    print("1.CALCULAR BINARIOS COMPLEMENTO A1 Y A2")
    print("2.CALCULAR HEXADECIMALES")
    print("3.SALIR")
    print("")
    op = int(input("Ingrese una opción: ")) #Menu de opciones





                
                    
    
        
        
    


