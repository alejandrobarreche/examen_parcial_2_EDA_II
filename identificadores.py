identificadores_fijos = [2441006710, 5581023627]

identificadores_variables = [
    2441006711, 2244100671, 2451006710, 5558102362, 2244100871,
    5227816305, 5282716305, 2441007611, 2441000675, 2441886770,
    2414006710, 5527816305
]

def identificadores_que_validan_primera_cifra(identificador):
    lista = []
    for i in identificadores_fijos:
        if int(str(abs(identificador))[0]) == int(str(abs(i))[0]):
            lista.append(i)
    return lista

def generar_diccionario_de_permutaciones(identificador_variable, identificador_fijo):
    identificador_variable_str = str(identificador_variable)
    identificador_fijo_str = str(identificador_fijo)
    longitud_fijo = len(identificador_fijo_str)

    if len(identificador_variable_str) < longitud_fijo:
        identificador_variable_str = identificador_variable_str.zfill(longitud_fijo)
    elif len(identificador_variable_str) > longitud_fijo:
        identificador_variable_str = identificador_variable_str[:longitud_fijo]

    rotaciones = {
        int(identificador_variable_str[i:] + identificador_variable_str[:i]): 0
        for i in range(longitud_fijo)
    }
    return rotaciones

def mirar_la_clave(num1, num2):
    """
    Compara dos números (como cadenas) y calcula la cantidad de saltos
    entre coincidir y no coincidir. Retorna el número de saltos.
    """
    saltos = 0
    ultima_coincidencia = None

    for i in range(len(str(num1))):
        coincide = int(str(num1)[i]) == int(str(num2)[i])  # Verificar si las cifras coinciden

        if ultima_coincidencia is not None and coincide != ultima_coincidencia:
            saltos += 1

        ultima_coincidencia = coincide
    return saltos


def comparar_cifras_y_validar(numero_fijo, diccionario):
    clave_0 = list(diccionario.keys())[0]


    for clave in diccionario.keys():
        for cifra_fijo, cifra_clave in zip(str(numero_fijo), str(clave)):
            if cifra_fijo == cifra_clave:
                diccionario[clave] += 1


        if diccionario[clave] >= 7:
            if mirar_la_clave(clave, numero_fijo) > 3:
                return False

            return True  # Si se cumple la condición, retornar True

    return False  # Si no se cumple la condición, retornar False

# Procesar identificadores variables
def main():
    for identificador_variable in identificadores_variables:
        identificadores_validos = identificadores_que_validan_primera_cifra(identificador_variable)
        encontrado = False  # Bandera para determinar si se encuentra un match

        for identificador_fijo in identificadores_validos:
            diccionario_permutaciones = generar_diccionario_de_permutaciones(identificador_variable, identificador_fijo)
            if comparar_cifras_y_validar(identificador_fijo, diccionario_permutaciones):
                print(f"{identificador_variable} es igual a {identificador_fijo}")
                encontrado = True
                break  # Salir del bucle una vez encontrado un match

        if not encontrado:
            print(f"{identificador_variable} es nuevo")

if __name__ == "__main__":
    main()