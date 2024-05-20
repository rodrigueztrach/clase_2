# ejercicio 1.1 

#Escribir un programa que solicite al usuario un
#numero entero y compruebe si un número es
#mayor o menor que 10


#pedimos que ingrese el usuario 

numero = int(input(" digite numero "))



#procedimiento  

if numero > 10:
                  print(" el numero es mayor a 10 ")                  
else:
                  print( " el numero es menor ")
#ejercicio 1.2


#Escribir un programa que solicite al usuario un
#numero decimal y se almacene como el mayor,
#luego pida otro numero decimal y compruebe si
#es mayor, menor o igual que el numero mayor
#registrado.

mayor = float(input(" digite el primer numero( decimales):"))

numero = float(input(" digite segundo numero(decimales):" ))


if mayor > numero :
                  print(f"el primer numero es mayor que  { mayor } que el segundo {numero}")
elif mayor < numero :
                  print(f"el numero es { numero } es menor que: { mayor }")  
else: 
                  print(f"el numero mayor es { mayor} es igual a { numero }") 

# Ejercicio 2.1 

#Escribir un programa que lea un número del usuario
#y muestre un mensaje indicando si el número es mayor
#que 10 y menor que 20, mayor que 20 o menor que 10.

numero = int(input(" digitar numero "))

if numero > 10:

                  if numero < 20 :
                                    print(" entonces es mayor que 10 y menor que 20 ") 
                  else:
                                    print(" entonces es mayor que 20  ")
else:
                  print (" entonces seria menor a 10 ")


#ejercicio 2.2 

if numero %2 == 0: 
                  
                  
                  if numero > 0:
                                    print(" el numero par es positivo ")
                  else: 
                                    print(" el numero par es negativo ")
else:
                  if numero > 0: 
                                    print(" el numero es impar positivo ")
                  
                  else: 
                                    print(" el numero impar negativo ")
                                    
                                    
if numero == 0: 
                  print(" el numero es 0 ")

#ejercicio 3
#números, el primer número se almacenará como el
#mayor, el segundo número se comparará con el primero
#el operador lógico and para realizar las comparaciones.

# 3.1
mayor = 0

menor = 0


mayor = int(input( "ingresar primer numero: "))

menor = int(input( "ingresar segundo numero: "))


if numero > numero != 0.0:
                  
                  mayor = numero 
                  
elif numero == mayor:
                  
                  print(" los numeros son iguales ")

else: 
                  
                  print( " el segundo numero es menor que el primero ")



#ejercicio 3.2

numero = float(input(" ingresar numero "))

if (numero >= 1 and numero <=  100 ) or numero < 0 : 
                  print( " el numero esta en el rango [1, 100] o es negativo")
else:
                  print( " el numero no cumple con las condiciones indicadas")


#tarea 


edad = 18 

nacionalidad = " si "


edad = int(input(" digite edad "))

if edad <= 18 and nacionalidad == " si ": 
                  print(" entonces si puede votar ")
                  
else:
                  (" no puede votar ")