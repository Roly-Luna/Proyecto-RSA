# Esta funcion revisa si un numero entero es primo
# Divide el numero entre todos los anteriores para verificar que no tenga divisores exactos
def es_primo(numero: int) -> bool:
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

# Esta funcion calcula el Maximo Comun Divisor (MCD) de dos numeros enteros
# Es fundamental para saber si dos numeros son coprimos
def calcular_mcd(a: int, b: int) -> int:
    while b != 0:
        resto = a % b
        a = b
        b = resto
    return a

# Esta funcion busca y devuelve una lista de posibles valores para la clave publica 'e'
# Selecciona los numeros que son coprimos con la funcion de Euler (phi)
def obtener_posibles_e(phi: int) -> list:
    lista_opciones_e = []
    for i in range(2, phi):
        if calcular_mcd(i, phi) == 1: 
            lista_opciones_e.append(i)
            if len(lista_opciones_e) == 10: 
                break
    return lista_opciones_e

# Esta funcion aplica el Algoritmo Extendido de Euclides.
# Sirve para calcular el inverso modular, que sera el valor base de la clave privada 'd'.
def algoritmo_euclides_extendido(e: int, phi: int) -> int:
    d = 0
    d_anterior = 1
    r = phi
    r_anterior = e
    while r != 0:
        cociente = r_anterior // r
        
        r_temporal = r
        r = r_anterior - (cociente * r)
        r_anterior = r_temporal
        
        d_temporal = d
        d = d_anterior - (cociente * d)
        d_anterior = d_temporal
        
    if d_anterior < 0:
        d_anterior = d_anterior + phi
        
    return d_anterior

# Esta funcion devuelve una lista con posibles valores validos para 'd'.
# Incluye el valor base calculado por Euclides y otros valores congruentes.
def obtener_posibles_d(e: int, phi: int) -> list:
    valor_d_base = algoritmo_euclides_extendido(e, phi)
    lista_opciones_d = [valor_d_base, valor_d_base + phi, valor_d_base + (2 * phi)]
    return lista_opciones_d