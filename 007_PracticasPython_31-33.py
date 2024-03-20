# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 23:41:50 2024

@author: ASPIRE

Practica 007
"""

"""
Este programa es la union de varios capítulos: 31, 32, 33
Donde se aprende a manejar Bucles
"""
titulo = "\n\t\tEsta práctica fue realizada por Juan Pablo Vázquez"#Se crea una variable con el titulo de toda la práctica
frase1 = "\n\nEn esta práctica aprenderemos a usar Diccionarios"
frase2 = "\nA guardar y buscar valores dentro del diccionario asi como su edición entre otras cosas\n"
print (titulo.title())#Se le da formato de titulo a la variable al momento de mostrarla en pantalla
print (frase1+frase2) #Se concatenan ambas variables formando oraciones completas

teclado1 = { #se crea un diccionario que contiene dos partes, claves y valores
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
}

teclado2 = { #se crea un diccionario que dos partes, claves y valores
	'Categoría': 'Teclados',
	'Modelo': 'Corsair K55 RGB',
	'Precio': '59,99'
}

consulta1 = teclado2['Modelo']#en una variable se guarda la informacion del diccionario del apartado 'Modelo'
consulta2 = teclado2['Precio']#en una variable se guarda la informacion del diccionario del apartado 'Precio'

print("El modelo",consulta1,"tiene un precio de",consulta2)

print("\n")#salto de linea para diferenciar informacion en consola
for x in teclado1:#el for guarda en x cada categoria del diccionario
    print(x,"=",teclado1[x],".")#se muestra tanto la categoria como el valor de la categoria


del teclado1 #se elimina el diccionario completo
del teclado2['Categoría'] #se elimina solo una parte del diccionario 2
del teclado2['Precio']
print("\n",teclado2)#muestra todo lo que queda del diccionario que es solo el modelo



