# Esta funcion crea y retorna un diccionario base con el abecedario y el espacio.
# A=0, B=1 ... Z=25, Espacio=26.
def generar_diccionario() -> dict:
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
    diccionario_letras = {}
    contador = 0
    for letra in alfabeto:
        diccionario_letras[letra] = contador
        contador += 1
    return diccionario_letras

# Esta funcion encripta el texto filtrando simbolos extranios pero manteniendo letras y espacios.
def encriptar_texto(texto: str, e: int, n: int, diccionario: dict) -> list:
    texto_mayusculas = texto.upper() 
    
    texto_limpio = ""
    for caracter in texto_mayusculas:
        if caracter in diccionario:
            texto_limpio += caracter
            
    lista_cifrada = []
    for caracter in texto_limpio:
        numero_base = diccionario[caracter]
        valor_cifrado = (numero_base ** e) % n
        lista_cifrada.append(valor_cifrado)
        
    return lista_cifrada