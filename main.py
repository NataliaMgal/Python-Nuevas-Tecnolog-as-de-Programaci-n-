#Soy un comentario de linea

'''

Soy un comentario de bloque

'''

#Variables en python
nombreUsuario='Natalia Morales'
#Salida en consola
#print("Hola buenas noches")
#Unir mensajes con variables (concatenar)
#print("su nombre es",nombreUsuario)
#fprint de python (otra forma de concatenar)
#print(f'su nombre es {nombreUsuario}')

#variables datos primitivos
#Para declarar un boolean comienza con la primera letra en mayuscula
edadUsuario = 19
estaturaUsuario = 1.60
esHinchaDelMejor= False
nombre='Natalia Morales'
#print(f'Mi nombre es {nombre} y sos hincha del mejor? {esHinchaDelMejor} ')

#entrada de datos por consola 
numero1=int(input("Digita un numero entero: "))
numero2=int(input("Digita otro numero entero: "))

suma=numero1+numero2
print(f'la suma de {numero1} + {numero2}= {suma}')

#las condiciones logicas (IF)
#No se usan las llaves y se debe tabular para poder que funcione
if(numero1>0):
    print("soy un numero positivo")
else:
    print("soy un numero negativo")    


