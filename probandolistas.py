#este code sera para probar un codigo comun del proyecto
#[]
Nombres_de_pacientes = [

    ('Juan Redondo', '1290346'),
    ( 'jazmin Hurtado', '123456'),

                       ]
#para hacer calculos deberemos color alfrente de input el tipo
#de variable que es ejm: "int(input())"
nombre = input("digite el nombre del paciente ")

print(f"el nombre del paciente es {nombre}")

#este es la funcion a usar para agregasr un nombre al final de una lista
Nombres_de_pacientes.append(nombre)

print(Nombres_de_pacientes)

DNI = input("digite el el DNI del paciente: ")
print(DNI in Nombres_de_pacientes)

"""
def leer_personas(lista):
    nombre = input("digite el nombre del paciente ")
    DNI = input("digite el el DNI del paciente: ")
    print(f"el nombre del paciente es {nombre} y su DNI es {DNI}")
    lista.append((nombre,DNI))
    
def load_file(ruta,lista):
    f = open(ruta, "r")
    for line in f.readlines():
        data = line.split(" ")
        nombre = data[0]
        dni = data[1]
        lista.append((nombre,dni))
    f.close()

def save_file(ruta,lista):
    f = open(ruta, "w")
    for element in lista:
        f.write(element[0])
        f.write(" ")
        f.write(element[1])
        f.write("\n")
    f.close()

# Testing the functions 
Nombres_de_pacientes = []
leer_personas() # cada vez que se llame se pedira que se ingresen los datos para  una persona
leer_personas()

load_file("my_file.txt",Nombres_de_pacientes) # si quieres cargar la lista de un archivo de nombre my_file.txt, tu escoge el nombre
save_file("my_file.txt",Nombres_de_pacientes) # si quieres guardar la lista en un archivo de nombre my_file.txt, tu escoge el nombre

"""
