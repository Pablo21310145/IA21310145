# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 11:27:12 2024

@author: ASPIRE

Practica 005
"""

"""
Este programa es la union de varios capítulos: 21, 22, 23, 24, 25, 26
Donde se aprende a manejar Condicionales
"""
titulo = "\n\t\tEsta práctica fue realizada por Juan Pablo Vázquez"#Se crea una variable con el titulo de toda la práctica
frase1 = "\n\nEn esta práctica aprenderemos a usar Condicionales"
frase2 = "\nTales como el condicional if o el complemento else, inputs entre otras cosas\n"
print (titulo.title())#Se le da formato de titulo a la variable al momento de mostrarla en pantalla
print (frase1+frase2) #Se concatenan ambas variables formando oraciones completas

num1 = 15 #se crea una variable para guardar un valor numérico y pueda ser comparado mas adelante
num2 = 20 #se crea una variable para guardar un valor numérico para comparar
num3 = 1450
num4 = 60
color = 'Rojo' #Se crea unavariable que contiene el string 'Rojo'
tupla = ('Rojo','Azul','Morado','Blanco')

if num1 < num2:  #Se compara si el valor de la primer variable es menor al de la segunda
    print("Se ejecuta el primer if.") #Al ser menor, la condicional retorna un valor de 'True' y se ejecuta el codigo

if num3 > num4: #Se compara si el valor de la primer variable es mayor al de la segunda
    print("Se ejecuta el segundo if.") #Al ser mayor, la condicional retorna un valor de 'True' y se ejecuta el codigo

num4 = 1450 #Se modifica el valor de la variable
if num3 != num4:  #Se compara si el valor de la primer variable es diferente al de la segunda
    print("Se ejecuta el tercer if.") #Al ser igual, la condicional retorna un valor de 'False' y no se ejecuta el codigo


if color == 'Rojo': #se compara si el valor contenido en la variable 'color' es igual a 'Rojo'
    print("\nEl color es Rojo.") #si el valor es igual la condicional retorna un valor de 'True' y se ejecuta el codigo
else:   #Si la condicional retorna un valor de 'False' se ejecuta esta parte del codigo, de lo contrario no se ejecuta
    print("\nEl color no es Rojo") #Dadas las condiciones del codigo en su estado actual, este mensaje no deberia aparecer en pantalla 
    

edad = int(input("\n¿Cuál es tu edad?\n"))
"""
La variable edad sera igual a lo introducido por el usuario
Se pregunta cual es la edad y ese valor será registrado por el metodo input()
Se guarda como un string
con el metodo int()se convierte ese valor de string a un valor nomerico int que puede ser comparado facilmente
"""
if edad <= 0: #se compara el valor contenido en la variable edad
	print("Nadie puede tener esa edad.") #Si la variable es menor o igual a 0 se ejecutara esta parte del codigo mostrando el mensaje
elif edad >= 1 and edad < 18:#la funcion 'and' busca que ambas condiciones se cumplan al mismo tiempo
	print("Eres menor de edad.")
elif edad >= 18 and edad <= 45:#Si cualquiera de las dos condiciones no se cumple, ese codigo no se ejecuta
	print("Empiezas la vida de adulto.")
elif edad > 45 and edad <= 100:
	print("Deberias pensar en tu retiro.")
elif edad > 100 and edad <= 120:
	print("No es facil llegar a vivir tanto.")
else: #Si ninguna de las condicionales anteiores devolvio un valor de 'True' se ejecutara esta parte del codigo
	print("Edad no válida.")


opcion = input("\n¿Que color de pintura buscas?\n")#Se crea una variable en la cual se guardara el mensaje introducido por el usuario
#Se usa sin el metodo int pues no es un valor numerico, tiene que ser tipo string
if opcion in tupla[0]:#Se busca el valor guardado en la variable dentro de la tupla, si es encontrado, el condicional devuelve 'True'
    print("El color aun esta disponible")
elif opcion in tupla[1]:#se busca en la siguiente posicion si el valor introducido por el usuario se encuentra en la tupla
    print("El color aun esta disponible")
elif opcion in tupla[2]:
    print("El color aun esta disponible")
elif opcion in tupla[3]:
    print("El color aun esta disponible")
else:#si el valor introducido por el usuario no coincide con ninguno de los valores guardados en la tupla se ejecuta esta parte del codigo
    print("El color no está disponible")
"""
Se pueden usar varios if individuales para buscar el valor y el resultado no cambiaria
if valor 0 ==...
if valor 1 ==...
if valor 2 ==...
"""