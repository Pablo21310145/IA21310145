# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 10:48:20 2024

@author: ASPIRE

Practica 004
"""

"""
Este programa es la unión de varios capítulos: 19, 20
Donde se aprende a manejar tuplas y su conversion a listas
"""
titulo = "\n\t\tEsta práctica fue realizada por Juan Pablo Vázquez"#Se crea una variable con el titulo de toda la práctica
frase1 = "\n\nEn esta práctica aprenderemos a usar tuplas"
frase2 = "\nAsi como aprender a utilizar valores de tuplas, operar con ellos entre otras cosas\n"
print (titulo.title())#Se le da formato de titulo a la variable al momento de mostrarla en pantalla
print (frase1+frase2) #Se concatenan ambas variables formando oraciones completas


color = ('Rojo','Azul','Verde','Amarillo','Marrón','Lila','Negro','Rosa','Blanco','Naranja')#Creamos una variable que contiene una tupla con varios string dentro
colorLista = ['Rojo','Azul','Verde','Amarillo','Marrón','Lila','Negro','Rosa','Blanco','Naranja']#Creamos una variable que contiene una listade elementos
numeros = (10,1,5,11)#Creamos una variable que contiene una tupla de numeros
operacion = numeros[0]-numeros[1]+numeros[2]+numeros[3]#creamos una variable que guarda el resultado de operaciones con la tupla
print("El valor guardado en la segunda posicion de la tupla es",color[1])#Mostramos en pantalla el valor de la segunda posicion de la tupla igual que con cualquier lista
print("Operamos con los números contenidos en la tupla para obtener",operacion)


print("\nAhora cambiemos el tipo de una lista a tupla y corroboremos si se ha cambiado")
tupla = tuple(colorLista)#Se cambia el tipo de variable de una lista a una tupla con el metodo tuple() y se guarda en una variable llamada 'tupla'
print(type(tupla))#Corroboramos el tipo de la variable para saber si se ha cambiado correctamente
#Se puede realizar la operacion inversa y convertir una tupla en lista con el metodo list()