# PROYECTO #2 - GELSY SONNESSA / GIANCARLO ESPOSITO
# Módulo validation (1. valInt(), 2. valFloat(), 3. valComplex(), 4. valList())

# FUNCIÓN PARA VALIDACIÓN DE NÚMEROS ENTEROS:
def valInt(arg, intervalo=None):
    if isinstance(arg,int):
        if intervalo is None:
            return True
        elif type(intervalo) == list:
            if len(intervalo) >= 2:
                if intervalo[0] < intervalo[-1]:
                    for valor in intervalo:
                        if type(valor) == int:
                            if arg >= intervalo[0] and arg <= intervalo[-1]:
                                return True
                            else:
                                return False
                        else:
                            raise TypeError("La lista debe contener valores numéricos enteros")
                else:
                    raise ValueError("La valores numéricos deben estar ordenados de forma creciente")
            else:
                raise ValueError("La lista debe contener al menos 2 valores")

        elif type(intervalo) == tuple:
            if len(intervalo) >= 2:
                if intervalo[0] < intervalo[-1]:
                    for valor in intervalo:
                        if type(valor) == int:
                            if arg >= intervalo[0]+1 and arg <= intervalo[-1]-1:
                                return True
                            else:
                                return False
                        else:
                            raise TypeError("La tupla debe contener valores numéricos enteros")
                else:
                    raise ValueError("La valores numéricos deben estar ordenados de forma creciente")
            else:
                raise ValueError("La tupla debe contener al menos 2 valores")
        else:
            raise TypeError("El segundo argumento debe ser una lista o tupla")
    elif type(arg)==str:
        raise TypeError("Debe ingresar un número entero, no un 'str'")
    else:
        return False



# FUNCIÓN PARA VALIDACIÓN DE NÚMEROS FLOTANTES:
def valFloat(arg, intervalo=None):
    if type(arg) == float:
        if intervalo is None:
            return True
        elif type(intervalo) == list:
            if len(intervalo) >= 2:
                if intervalo[0] < intervalo[-1]:
                    for valor in intervalo:
                        if type(valor) == int:
                            if arg >= intervalo[0] and arg <= intervalo[-1]:
                                return True
                            else:
                                return False
                        else:
                            raise TypeError("La lista debe contener valores numéricos enteros")
                else:
                    raise ValueError("La valores numéricos deben estar ordenados de forma creciente")
            else:
                raise ValueError("La lista debe contener al menos 2 valores")

        elif type(intervalo) == float:
            if len(intervalo) >= 2:
                if intervalo[0] < intervalo[-1]:
                    for valor in intervalo:
                        if type(valor) == int:
                            if arg >= intervalo[0]+1 and arg <= intervalo[-1]-1:
                                return True
                            else:
                                return False
                        else:
                            raise TypeError("La tupla debe contener valores numéricos enteros")
                else:
                    raise ValueError("La valores numéricos deben estar ordenados de forma creciente")
            else:
                raise ValueError("La tupla debe contener al menos 2 valores")
        else:
            raise TypeError("El segundo argumento debe ser una lista o tupla")
    elif type(arg)==str:
        raise TypeError("Debe ingresar un número entero, no un 'str'")
    else:
        return False


# FUNCIÓN PARA VALIDACIÓN DE NÚMEROS COMPLEJOS:
def valComplex(arg, intervalo=None):
    if type(arg) == complex:
        if intervalo is None:
            return True
        elif type(intervalo) == list:
            if len(intervalo) >= 2:
                if intervalo[0] < intervalo[-1]:
                    for valor in intervalo:
                        if type(valor) == int:
                            if abs(arg) >= intervalo[0] and abs(arg) <= intervalo[-1]: # La función "abs()" se emplea para obetener el módulo del número complejo
                                return True
                            else:
                                return False
                        else:
                            raise TypeError("La lista debe contener valores numéricos enteros")
                else:
                    raise ValueError("La valores numéricos deben estar ordenados de forma creciente")
            else:
                raise ValueError("La lista debe contener al menos 2 valores")

        elif type(intervalo) == tuple:
            if len(intervalo) >= 2:
                if intervalo[0] < intervalo[-1]:
                    for valor in intervalo:
                        if type(valor) == int:
                            if abs(arg) >= intervalo[0]+1 and abs(arg) <= intervalo[-1]-1:
                                return True
                            else:
                                return False
                        else:
                            raise TypeError("La tupla debe contener valores numéricos enteros")
                else:
                    raise ValueError("La valores numéricos deben estar ordenados de forma creciente")
            else:
                raise ValueError("La tupla debe contener al menos 2 valores")
        else:
            raise TypeError("El segundo argumento debe ser una lista o tupla")
    elif type(arg)==str:
        raise TypeError("Debe ingresar un número entero, no un 'str'")
    else:
        return False

arg = "hola"
Lp = (6,8,9)
print(valInt(arg,Lp))