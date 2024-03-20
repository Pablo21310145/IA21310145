# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 12:21:53 2024

@author: ASPIRE

Practica 003
"""

"""
Este programa es la unión de varios capítulos: 10, 11, 12, 13, 14, 15, 16, 17, 18
Donde se aprende a manejar listas de datos
"""
titulo = "\n\t\tEsta práctica fue realizada por Juan Pablo Vázquez"#Se crea una variable con el titulo de toda la práctica
frase1 = "\n\nEn esta práctica aprenderemos a usar listas de variables"
frase2 = "\nAsi como aprender a utilizar valores de listas negativas, agregar y eliminar valores entre otras cosas\n"
print (titulo.title())#Se le da formato de titulo a la variable al momento de mostrarla en pantalla
print (frase1+frase2) #Se concatenan ambas variables formando oraciones completas

color = ["Rojo","Azul","Verde","Amarillo","Marrón","Lila","Negro","Rosa","Blanco","Naranja"] #Se crea una lista de valores contenidos en la variable "color" 
posi = ["Tres","Dos","Cinco","Cuatro","Uno"]#Se crea una lista de valores contenidos en la variable "posi" 

print("Creamos una lista con colores:\n",color)
print("El color en la posición 3 es",color[3])#se busca el valor en la posicion 3 del arreglo para mostrarlo en pantalla
#Buscamos los colores Rojo y Rosa
print("El color",color[0],"se encuentra en la posición 0")#El color Rojo al ser el primer elemento de la lista, se encuentra en la posicion 0
print("El color",color[7],"se encuentra en la posición 7")#El color Rosa se encuentra en la posicion 7


print("\nBuscamos los colores Naranja, Amarillo, Lila, Blanco y Rojo con valores negativos")#Buscamos algunos de los valores dentro de la lista utilizando valores negativos
print("\nSi utilizamos valores negativos para buscar los colores podemos encontrar el color",color[-1],' en la posición "-1"')
print("El color",color[-7],' en la posición "-7"')
print("El color",color[-5],' en la posición "-5"')
print("El color",color[-2],' en la posición "-2"')
print("El color",color[-10],' en la posición "-10"')


print("\nBuscamos los colores Azul, Marrón, Negro y Rosa para eliminarlos de la lista con la función 'del'")#Buscamos algunos de los valores dentro de la lista para eliminarlos
print("\nMostramos la lista completa:\n",color)#mostramos la lista completa antes de modificarla
del color[1]#Borramos el valor en la posicion 1 de la lista
del color[3]#Tomar en cuenta que al borrar un valor de la lista las posiciones se modifican por lo que ahora el marron esta en la posicion 3 y no en la 4
del color[-4]#Borramos el valor en una posicion negativa de la lista
del color[-3]#La funcion del solo borra elementos de los cuales conocemos su posición
print("\nAhora mostramos la lista despues de borrar los valores para comprobar que se han eliminado correctamente:")
print(color)#Mostramos nuevamente la lista


print("\nDe los valores restantes de la lista eliminamos los colores Amarillo y Rojo con la función 'remove'")
color.remove("Rojo")#Buscamos el valor "Rojo" dentro de la lista para eliminarlo con la funcion .remove
color.remove("Amarillo")#La función .remove solo elimina valores que conoces que estan en la lista
print("\nMostramos la lista nuevamente despues de borrar los valores para comprobar que se han eliminado correctamente:")
print(color)#mostramos la lista para comprobar los valores que quedan


print("\nDe los colores que quedan quitaremos los colores Verde y Blanco y los pondremos en otra lista")
caja1 = color.pop(0)#con la funcion pop quitamos el elemento 0 de la lista y se guarda en la variable caja1
caja2 = color.pop(1)#con la funcion pop quitamos el elemento 1 de la lista y se guarda en la variable caja2
color2 = [caja1,caja2]#creamos una nueva lista para guardar los valores que quitamos de la lista anterior
print("La lista original queda como:",color,"\nLos valores que guardamos en una nueva lista son:",color2)#mostramos ambas listas


print("\nQuedan muy pocos colores, agregaremos mas con la función '.append()'")#utilizaremos la funcion .append() para agregarnuevos valores a la lista
color.append("Fuxia")#Agrega el valor "Fuxia" a la lista en la ultima posición
color.append("Celeste")#Agrega el valor "Celeste" a la lista en la ultima posición
print(color)


color = ["Rojo","Azul","Verde","Amarillo","Marrón","Lila","Negro","Rosa","Blanco","Naranja"]#Reinicio la lista de colores para agregar mas valores con el metodo insert()
print("\n\nVolvamos a la lista de colores original\n",color,"\n\nA esta lista agregaremos mas colores con el metodo 'insert()'")
color.insert(-4,"Magenta")#Insertamos el valor "magenta" con el metodo .insert() el cual requiere dos valores que son la posición y el valor a insertar, en ese orden
color.insert(-1,"Turquesa")#Insertamos el valor "Turquesa" en la posicion -1
print(color)


print("\nMostremos la lista en orden alfabetico descendente:")#Utilizamos la funcion sort() para ordenar la lista
color.sort(reverse=True)#agregamos la palabra reverse para que sea en orden descendente y la palabra True tiene que ser con mayúscula
print(color)
"""
El metodo .sort() tiene un efecto permanente sobre la lista por lo que los valores quedaran guardados en el nuevo orden
De requerirse una solucion temporal se puede utilizar print(sorted(color))
print(sorted(color)) los ordena solo para el momento de mostrar los valores
Dentro del parentesis, la palabra reverse indica que sera en orden inverso, es decir descendente
La palabra True tiene que ser mayúscula
"""

cantidad_colores = len(color)#El metodo len() permite contabilizar la cantidad de elementos contenidos en una lista
print("\n\nAl final nuestra lista terminó con",cantidad_colores,"colores")


