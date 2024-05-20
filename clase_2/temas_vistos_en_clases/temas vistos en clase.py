#temas vistos en clases 

#condicionales_simples 

numero = 12

if numero > 10:
                         print(" es mayor que 10. ")
                         
#condicional_doble 

#veamos si es numero es mayor o menor

numero = 10 

if numero >= 11: 
                         print(" es mayor que 11. ")
else:
                         print (" es menor que 11. ")


#operadores relacionales 

#comparemos estos numeros 


tabla1 = 20 

tabla2 = 34 

if tabla1 == tabla2:
                         print(" las tablas son iguales ")
else:
                         print(" las tablas son diferentes ")

#operador AND 

#veamos si estas combinaciones son verdaderas 

sexo = "hombre" 

edad = 17 

if edad >=18 and sexo == "hombre":
                         print( " puede ingresar ")
else:
                         print( " no puede ingresar ")
                         
#operador or 

#si tiene 18 y es mujer puede ser elegible  

edad = 17

sexo = " mujer "

if edad >= 18 or sexo == "hombre": 
                         print ("queda elegible.")
                         
else:
                         print(" no queda elegible ")
                         
#operador not 

#verifiquemos si califica 

edad = 18

if not edad >= 19 :
                         print( " no ingresa ")
else:
                         print(" si ingresa ")