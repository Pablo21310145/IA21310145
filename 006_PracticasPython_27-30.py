# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 22:46:43 2024

@author: ASPIRE

Practica 006
"""

"""
Este programa es la union de varios capítulos: 27, 28, 29, 30
Donde se aprende a manejar Bucles
"""
titulo = "\n\t\tEsta práctica fue realizada por Juan Pablo Vázquez"#Se crea una variable con el titulo de toda la práctica
frase1 = "\n\nEn esta práctica aprenderemos a usar Bucles"
frase2 = "\nTales como el bucle 'while' y el bucle 'for' entre otras cosas\n"
print (titulo.title())#Se le da formato de titulo a la variable al momento de mostrarla en pantalla
print (frase1+frase2) #Se concatenan ambas variables formando oraciones completas

x = 0 #Se crea una variable que inicia con valor 0
color = ('rojo','azul','verde','amarillo') # se crea una tupla que almacena colores

while x <= 15: #se crea un bucle while que se ejecutará hasta que x sea mayor o igual que 15
    print(x) #se muestra que el valor de x sigue siendo menor o igual que 15
    x += 5 #se aumenta el valor de x en 5

print("\n")#se genera un salto de linea para diferenciar las salidas en consola
x = 0 #se restablece el valor de la variable a 0
while x >= -100: #se genera un nuevo bucle hasta que x sea menor o igual a -100
    print(x) # se muestra el valor de x
    x -= 20 # se decrementa el valor de x en 20

print("\n")#se genera un salto de linea para diferenciar las salidas en consola
x = 10 #a la variable x se le da un valor inicial de 10
while x >= 0:# se crea un bucle que se ejecutará hasta que x llege a 0
    print("El valor de x es:",x)
    x -= 1 #se reduce el valor de 1 en 1

print("\n")#se genera un salto de linea para diferenciar las salidas en consola
x = 0#se reinicia la variablle a 0
while x <= 30:#se crea un bucle hasta que x sea igual o mayor a 30
    x += 1#se incremente el valor de x en 1
    if x == 15:#condicional para saber si el valor de x alcanza 15
        print("Se sompió la ejecución del bucle cuando x valía:",x)
        break#al llegar al valor de 15 el comando break rompe el ciclo aunque no se cumpliera la condición inicial
    if x == 4 or x == 6 or x == 10:#al llegar a cualquiera de los 3 valores se ejecutara el siguiente codigo
        print("Se saltó el valor",x,"de x")
        continue#se interrumple el ciclo actual sin terminar el ciclo por completo
    print("El valor del bucle es:",x)#durante cada ciclo del buble se estara mostrando el valor actual de x


print("\n")
for x in color:#Se crea un bucle for que busca entre cada valor almacenado en la tupla
    print("El color es:",x,".")#se muestra cada valor almacenado en la tupla


print("\n")
for x in range(7,700, 100):#se crea un bucle forque inicia en 7 hasta llegar a 700 con incrementos de 100 en 100
	print("El valor del bucle es:",x)#se muestra en consola el valor de x
