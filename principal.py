import os
import matematica_rsa
import cifrado_rsa

# ==========================================
# FUNCIONES DE INTERFAZ Y UTILIDAD
# ==========================================

def mostrar_encabezado() -> None:
    print("======================================================")
    print("           SISTEMA CRIPTOGRAFICO RSA - UPC            ")
    print("======================================================")

def mostrar_instrucciones() -> None:
    os.system('cls')
    mostrar_encabezado()
    print("                   INSTRUCCIONES                      ")
    print("======================================================\n")
    print("1. Para ENCRIPTAR (Opcion 1):")
    print("   - Ingresa el texto que deseas ocultar.")
    print("   - Elige cuantos numeros primos usaras (minimo 2).")
    print("   - Ingresa los numeros primos (maximo 2 cifras).")
    print("   - Sigue los pasos para elegir tus claves 'e' y 'd'.")
    print("\n* Nota: La fase de Desencriptacion y guardado en Bloc")
    print("  de Notas sera implementada para la entrega final (100%).")
    print("\n======================================================")
    print("") 
    os.system("pause")


# ==========================================
# SUB-MODULOS DE LA FASE DE ENCRIPTACION
# ==========================================

def ingresar_datos_base() -> tuple:
    os.system('cls')
    mostrar_encabezado()
    print("                 FASE DE ENCRIPTACION                 ")
    print("======================================================\n")
    
    texto_ingresado = input("> Ingrese el texto que desea encriptar: ")

    while True:
        try:
            cantidad_primos = int(input("\n¿Cuantos numeros primos deseas usar? (Minimo 2): "))
            if cantidad_primos >= 2:
                break
            print("-> ERROR: Debes usar al menos 2 primos para que el RSA funcione.")
        except ValueError:
            print("-> ERROR: Por favor ingresa un numero entero.")

    print("\n--- Ingreso de Numeros Primos ---")
    lista_primos_ingresados = []
    
    for i in range(cantidad_primos):
        while True:
            try:
                primo_actual = int(input(f"Ingresa el primo #{i+1} (1 o 2 cifras maximo): "))
                
                if primo_actual > 99:
                    print("-> ERROR: El numero debe tener 1 o 2 cifras como maximo.")
                elif not matematica_rsa.es_primo(primo_actual):
                    print("-> RECHAZADO: El numero NO es primo. Corrigelo antes de continuar.")
                elif primo_actual in lista_primos_ingresados:
                    print("-> ERROR: Los numeros primos deben ser diferentes entre si.")
                else:
                    lista_primos_ingresados.append(primo_actual)
                    break 
            except ValueError:
                print("-> ERROR: Ingresa solo numeros enteros validos.")
                
    return texto_ingresado, lista_primos_ingresados


def mostrar_calculos_matematicos(lista_primos_ingresados: list) -> tuple:
    modulo_n = 1
    funcion_euler_phi = 1
    
    for primo in lista_primos_ingresados:
        modulo_n = modulo_n * primo
        funcion_euler_phi = funcion_euler_phi * (primo - 1)

    os.system('cls')
    mostrar_encabezado()
    print("             PASO 1: CALCULOS MATEMATICOS             ")
    print("======================================================\n")
    print(f"Numeros primos validados: {lista_primos_ingresados}\n")
    print(f"Calculo detallado del Modulo 'n'        : {modulo_n}")
    print(f"Calculo de la funcion de Euler 'phi(n)' : {funcion_euler_phi}")
    print("")
    os.system("pause")
    
    return modulo_n, funcion_euler_phi


def elegir_clave_publica(funcion_euler_phi: int) -> int:
    os.system('cls')
    mostrar_encabezado()
    opciones_clave_e = matematica_rsa.obtener_posibles_e(funcion_euler_phi)
    print("          PASO 2: SELECCION DE CLAVE PUBLICA 'e'      ")
    print("======================================================\n")
    print(f"Opciones de 'e' (deben ser coprimos con {funcion_euler_phi}):\n")
    print(f" -> {opciones_clave_e}\n")

    while True:
        try:
            clave_e_seleccionada = int(input("> Selecciona el valor de 'e' de la lista mostrada: "))
            if clave_e_seleccionada in opciones_clave_e:
                break
            print("-> ERROR: El valor debe ser estrictamente uno de la lista.")
        except ValueError:
            print("-> ERROR: Ingresa un numero entero valido.")
            
    return clave_e_seleccionada


def elegir_clave_privada(clave_e_seleccionada: int, funcion_euler_phi: int) -> int:
    os.system('cls')
    mostrar_encabezado()
    opciones_clave_d = matematica_rsa.obtener_posibles_d(clave_e_seleccionada, funcion_euler_phi)
    print("         PASO 3: SELECCION DE CLAVE PRIVADA 'd'       ")
    print("======================================================\n")
    print(f"Posibles valores para 'd' resolviendo congruencia (e*d = 1 mod phi):\n")
    print(f" -> {opciones_clave_d}\n")

    while True:
        try:
            clave_d_seleccionada = int(input("> Selecciona el valor de 'd' de la lista mostrada: "))
            if clave_d_seleccionada in opciones_clave_d:
                break
            print("-> ERROR: El valor debe ser estrictamente uno de la lista.")
        except ValueError:
            print("-> ERROR: Ingresa un numero entero valido.")

    return clave_d_seleccionada


# ==========================================
# ORQUESTADORES PRINCIPALES
# ==========================================

def opcion_encriptar() -> None:
    # Ingreso de datos
    texto_ingresado, lista_primos_ingresados = ingresar_datos_base()
    
    # Calculos matematicos
    modulo_n, funcion_euler_phi = mostrar_calculos_matematicos(lista_primos_ingresados)
    
    # Seleccion de claves
    clave_e_seleccionada = elegir_clave_publica(funcion_euler_phi)
    clave_d_seleccionada = elegir_clave_privada(clave_e_seleccionada, funcion_euler_phi)

    # Resumen y Cifrado
    os.system('cls')
    mostrar_encabezado()
    print("                 RESUMEN DE LAS CLAVES                ")
    print("======================================================\n")
    print(f" -> Clave Publica  : (n={modulo_n}, e={clave_e_seleccionada})")
    print(f" -> Clave Privada  : (n={modulo_n}, d={clave_d_seleccionada})\n")
    
    print("======================================================")
    print("[+] Aplicando el diccionario y procesando cifrado...")
    
    diccionario_sistema = cifrado_rsa.generar_diccionario()
    matriz_cifrada = cifrado_rsa.encriptar_texto(texto_ingresado, clave_e_seleccionada, modulo_n, diccionario_sistema)
    
    print(f"\nMensaje Cifrado Exitosamente:\n{matriz_cifrada}")
    print("\n[!] MODULO DE GUARDADO EN .TXT PENDIENTE PARA LA ENTREGA FINAL.")
    print("")
    os.system("pause")


def opcion_desencriptar() -> None:
    os.system('cls')
    mostrar_encabezado()
    print("   MODULO EN CONSTRUCCION PARA LA ENTREGA FINAL (100%)  ")
    print("======================================================\n")
    print("La lectura de archivos txt y el algoritmo matematico de")
    print("desencriptacion se integraran en la semana 11.")
    print("")
    os.system("pause")


def ejecutar_programa() -> None:
    while True:
        os.system('cls')
        mostrar_encabezado()
        print(" [1] ENCRIPTAR NUEVO MENSAJE")
        print(" [2] MOSTRAR INSTRUCCIONES")
        print(" [3] DESENCRIPTAR DESDE ARCHIVO (PROXIMAMENTE)")
        print(" [4] SALIR DEL SISTEMA")
        print("======================================================\n")
        
        opcion_elegida = input("Elige una opcion del menu (1-4): ")
        
        if opcion_elegida == '1':
            opcion_encriptar()
        elif opcion_elegida == '2':
            mostrar_instrucciones()
        elif opcion_elegida == '3':
            opcion_desencriptar()
        elif opcion_elegida == '4':
            print("\n[+] Cerrando el sistema criptografico... Hasta pronto!")
            break
        else:
            print("\n-> ERROR: Opcion no valida. Selecciona un numero del 1 al 4.")
            print("")
            os.system("pause")


if __name__ == "__main__":
    ejecutar_programa()