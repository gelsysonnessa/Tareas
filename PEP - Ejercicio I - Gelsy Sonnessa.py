# EJERCICIO I - PARCIAL 1

semilla = int(input("Ingrese un numero entero de al menos 4 digitos: "))
n = len(str(semilla))

intentos_fallidos = 0
for i in range(3):
  if n < 4:
    semilla = int(input("ERROR. Por favor, ingresa un numero entero de al menos 4 digitos: "))
    intentos_fallidos += 1
    n = len(str(semilla))
    
  if intentos_fallidos == 3 and semilla < 4:
    print("Lo sentimos, excediste la cantidad de intentos")
    quit()
    
cantidad = int(input("Ingrese la cantidad de numeros aleatorios que desea: "))

for j in range(cantidad):
    
  num_cuadrado = semilla**2
  
  inicio = (len(str(num_cuadrado)) - n)//2 # --> Las variables 'inicio' y 'fin' nos definen el rango donde se obtienen 
  fin = inicio + n                         # los numeros medios en función de la cantidad de digitos
  
  num_cuadrado = str(num_cuadrado)
  middle_digit = num_cuadrado[inicio:fin]
  semilla = int(middle_digit)
  num_aleatorio = str(semilla/10**n)

  if len(num_aleatorio) < n+2:
      num_aleatorio = num_aleatorio + '0' # completamos con 0 los números cuyos decimales < n (cantidad de digitos ingresados)
      
  print(num_aleatorio)
  