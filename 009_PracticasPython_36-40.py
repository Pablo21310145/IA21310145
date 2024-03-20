# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 00:46:19 2024

@author: ASPIRE

Practica 009
"""

"""
Este programa es la union de varios capítulos: 36, 37, 38, 39, 40, 41
Donde se aprende a manejar Bucles
"""
titulo = "\n\t\tEsta práctica fue realizada por Juan Pablo Vázquez"#Se crea una variable con el titulo de toda la práctica
frase1 = "\n\nEn esta práctica se inicia con programación orientada a objetos"
frase2 = "\nDesde su creacion hasta como mandar los datos que espera entre otras cosas\n"
print (titulo.title())#Se le da formato de titulo a la variable al momento de mostrarla en pantalla
print (frase1+frase2) #Se concatenan ambas variables formando oraciones completas

def colores (**kwargs):#se crea una funcion que espera argumentos especiales
	print("Este es el color " + kwargs['color1'] + '.')#se imprime en consola con los datos recibidos

colores(color1='rojo', color2='azul')#se llama a funcion enviando los datos


class Usuario1: # se crea una clase llamada usuario
	nombre = '' #uno de los atributos contenidos en la clase es una variable llamada nombre
	apellidos = ''#otro atributo contenido es una segunda variable llamada apellidos


usuario001 = Usuario1()#se crea un objeto que tiene los atributos contenidos en 'Usuario1()'

usuario001.nombre = 'Enrique'#se asignan valores a los atributos contenidos
usuario001.apellidos = 'Barros Fernández'

del Usuario1.nombre
