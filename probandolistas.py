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

