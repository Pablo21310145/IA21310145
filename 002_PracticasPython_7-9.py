# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 22:39:50 2024

@author: ASPIRE

Practica 002
"""

"""
Este programa es la unión de varios capítulos: 7, 8, 9
donde se aprende a manejar operaciones basicas con numeros
"""
titulo = "\n\t\tEsta práctica fue realizada por Juan Pablo Vázquez"
frase1 = "\n\nEn esta práctica aprenderemos a usar las operaciónes aritméticas de Python"
frase2 = "\nHaremos operaciones como:\n\t-Suma.\n\t-Resta.\n\t-Multiplicación.\n\t-División."
print (titulo.title())
print(frase1+frase2)


suma = 20 + 23 + 28 + 16 #Se crea una variable que contenga operaciones de de suma
resta = 20 - 23 - 17 - 22 - 18 - 14 - 13 #Se crea una variable que contenga operaciones de de resta
multi =1.891304348 * 20 * 23#Se crea una variable que contenga operaciones de multiplicacion
#El resultado ha sido un numero de coma flotante
div =5000/230/2 #Se crea una variable que contenga operaciones de
oper = 10 /5 + 15 - 17 #Se crea una variable que contenga multiples operaciones
decimal = 17.567383292929200234 #Se guarda un valor de muchos decimales en una variable
#Se guarda como valor float de forma automatica
expo = 2*2*2*2*2*2*2*2*2*2 #Sin utilizar la funcion exopnente se llega al resultado de 1024

print("\nPodemos sumar y obtener\n",suma,"\n\nPodemos restar y obtener numeros negativos como\n",resta)
print("\nAl multiplicar incluzo podemos obtener muchos decimales como el numero\n",multi,"\n\nPero se puede arreglar acotando los decimales\n",round(multi))
print("\nDejarlos tal como queden\n",div,"\n\nInclusive se pueden mostrar solo la cantidad que necesites como el cazo de\n",round(decimal,5))
print("\nO realizar multiples operaciones en una y obtener\n",oper)
print("\nSe pueden utilizar funciones de exponente o realizar las multiplicaciones necesarias para llegar al mismo resultado como en el número",expo)