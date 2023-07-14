# EJERCICIO II - PARCIAL 1

H = int(input("Ingrese la profundidad del pozo (en metros): "))
Ld = int(input("Ingrese lo que asciende el caracol durante el día (en metros): "))
Ln = int(input("Ingrese lo que desciende el caracol durante la noche (en metros): "))

posicion = Ld - Ln
L = 0
dias = 0

if posicion <= 0:
    print("El caracol nunca saldrá del pozo :(")
    
while Ld > 0:
    
    if posicion > 0:
        L += posicion
        dias += 1 # --> 24 horas
        
    if L + Ld >= H:
        break
        
print("El caracol tardó",dias,"días en salir del pozo") 

