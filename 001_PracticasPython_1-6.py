# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 18:28:41 2024

@author: ASPIRE

Practica 001
"""

"""
Este programa es la unión de varios capítulos: 1, 2, 3, 4, 5 y 6
donde se aprende a manejar variables
"""
frase1 = "\n\t\tEsta práctica fue realizada por Juan Pablo Vázquez" #Se guarda en una variable un string
frase2 = '\n\t\tMejor conocido como "John"\n\n' #Se guarda en una variable otro string
#Debido al escape de caracteres se debe utilizar comillas simples para poder mostrar comillas dobles en el interior del mensaje
frase3 = frase1 + frase2 #Se concatenan ambas variables formando oraciones completas

print (frase3.title()) #aplica el metodo title a una cadena al momento de imprimirla para darle formato

frase4 = "Hola mundo!"
frase5 = "\n\nEn esta práctica aprenderemos a usar las variables de Python"
mensaje = frase4 + frase5
"""
Creamos la variable "frase4" que contiene "Hola mundo!"
Por ley debe decir hola mundo
Creamos otra que contiene otro string y concatenamos ambas en una nueva variable
No hay necesidad de escribir ";" al final de cada linea u operacion como en otros lenguajes de programación
"""

a = 10 #Se crea una variable de tipo entero
b = 20 #No hay necesidad de definir el tipo de variable
c = a+b #La variable contiene la operacion reaizada con otras variables

print (mensaje) #Se muestra en pantalla el mensaje guardado

print ("\nEl primer valor es:",a,"\n\nEl segundo valor es:",b,"\n\nLa suma de ambos valores es:",c) 
"""
Se muestra en pantalla un mensaje seguido de un valor guardado en una variable
Se muestra otro mensaje seguido de otra variable
Se concatenan usando "," de forma que se puedan usar valores numericos y strings
Se muestra un mensaje con el resultado de la operacion realizada
"""

a = '20' #Modificamos el valor que guarda la variable y el tipo de dato que es
b = '24' #Ahora el valor queda registrado como string
c = a+b #Concatenamos los valores y guardamos el resultado en otra variable
print ("\nEl año actual es:",c)

cursos = "Hasta la fecha puedo programar en diferentes lenguajes como:\n\t-Python.\n\t-JavaScript.\n\t-Java.\n\t-PHP.\n\t-TypeScript.\n\t-C.\n\t-C++."
print(cursos)
"""
Se ha creado la variable "cursos" que contiene mucha informacion
Incluidos saltos de linea y tabuladores
Ahora solo se genera un print y se emite todo el mensaje
"""
