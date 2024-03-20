# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 00:03:00 2024

@author: ASPIRE

Practica 008
"""

"""
Este programa es la union de varios capítulos: 34 y 35
Donde se aprende a manejar Bucles
"""
titulo = "\n\t\tEsta práctica fue realizada por Juan Pablo Vázquez"#Se crea una variable con el titulo de toda la práctica
frase1 = "\n\nEn esta práctica aprenderemos a usar Funciones"
frase2 = "\nDesde su creacion hasta como mandar los datos que espera entre otras cosas\n"
print (titulo.title())#Se le da formato de titulo a la variable al momento de mostrarla en pantalla
print (frase1+frase2) #Se concatenan ambas variables formando oraciones completas


def suma(dato1, dato2): #se crea una funcion llamada suma que espera recibir dos datos
    resp = dato1 + dato2 # se crea una variable que contiene la suma de los dos datos recibidos
    print(resp)#se muestra en consola el valor de la variable, es decir la suma

suma(15,15)#se llama a la funcion y se le envian los dos datos que pide
suma(25,25)#se llama a la funcion y se le envian los dos datos que pide
suma(50000,7000)#se llama a la funcion y se le envian los dos datos que pide


def colores(*args): #se crea una funcion llamada colores que espera argumentos en general
	pass

colores('rojo', 'azul', 'verde', 'amarillo')#se envian cuatro argumentos a la función
colores('lila', 'negro', 'rojo')#se envian tres argumentos a la función
colores('rosa')#se envia un argumento a la función
colores('marrón', 'naranja')#se envian dos argumentos a la función


def colorines(*args):#se crea una funcion que espera argumentos en general
	print('\nEl color', args[1], 'es mi favorito.', 'El color', args[0], 'tampoco está mal.')#se muestra en consola una frase que usa los valores enviados

colorines('rojo', 'azul', 'verde', 'amarillo')#se llama a la funcion y se le envian los argumentos


def sumas(*args): #se crea una funcion llamada sumas que espera recibir los argumentos
    resp = args[0] + args[1] + args[2] + args[3] + args[4] # se crea una variable que contiene la suma de los dos datos recibidos
    print("\nEl resultado de la suma es:",resp)#se muestra en consola el valor de la suma

sumas(10, 15, 20, 30, 50)#se llama a la funcion y se le envian los argumentos que pide

"""
Tambien se existen metodos para trabajar con diccionarios pero debido a su naturaleza no es igual
Se utiliza algo llamado **Kwargs
Es decir que no esperas un argumento general sino un dato mas complejo
Tecnicamente los ejercicios de Python terminan aqui
Los demas temas, aunque interesantes, no requieren de mas codigos que den respuesta al problema
"""



