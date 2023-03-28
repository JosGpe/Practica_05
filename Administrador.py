import os
# Definicion de lista de segmentos de memoria
memoria = [(0, 1000), (0, 400), (0, 1800), (0, 700), (0, 900), (0, 1200), (0, 1500)]

# Leemos el archivo con los nombres y tamaños de los archivos a guardar
with open('archivos.txt') as f:
    archivos = f.readlines()
    archivos = [x.strip().split(', ') for x in archivos]
    archivos = [[nombre, int(tamano.replace('kb', ''))] for nombre, tamano in archivos]


while True:
    # Preguntamos al usuario qué algoritmo quiere utilizar
    os.system('cls')
    print('Elija un algoritmo de administración de memoria:')
    print('1. Primer ajuste')
    print('2. Mejor ajuste')
    print('3. Peor ajuste')
    print('4. Siguiente ajuste')
    print("\n")
    algoritmo = int(input('Escriba el número del algoritmo que desea utilizar: '))

    # Validamos la entrada del usuario
    if algoritmo < 1 or algoritmo > 4:
        print('Opción inválida. Intente de nuevo.')
        continue

    # Ejecutamos el algoritmo seleccionado

    # Primer ajuste
    if algoritmo == 1:  
        os.system('cls')
        print(memoria)
        print("\n")
        for archivo in archivos:
            nombre, tamano = archivo[0], int(archivo[1])
            asignado = False
            # Busca el primer segmento con suficiente espacio para el archivo
            for i, segmento in enumerate(memoria):
                if segmento[1] - segmento[0] >= tamano:
                    memoria[i] = (segmento[0], segmento[1] - tamano)
                    asignado = True
                    print(f'{nombre} asignado a segmento {i}')
                    break
            if not asignado:
                print(f'{nombre} no pudo ser asignado')
        print("\n")
        print(memoria)

    # Mejor ajuste
    elif algoritmo == 2:  
        os.system('cls')
        print(memoria)
        print("\n")
        for archivo in archivos:
            nombre, tamano = archivo[0], int(archivo[1])
            mejor_segmento = None
            # Busca el segmento disponible más pequeño que pueda contenerlo
            for segmento in memoria:
                if segmento[1] - segmento[0] >= tamano:
                    if mejor_segmento is None or (segmento[1] - segmento[0]) < (mejor_segmento[1] - mejor_segmento[0]):
                        mejor_segmento = segmento
            if mejor_segmento is not None:
                i = memoria.index(mejor_segmento)
                memoria[i] = (mejor_segmento[0], mejor_segmento[1] - tamano)
                print(f'{nombre} asignado a segmento {i}')
            else:
                print(f'{nombre} no pudo ser asignado')
        print("\n")
        print(memoria)

    # Peor ajuste
    elif algoritmo == 3:  
        os.system('cls')
        print(memoria)
        print("\n")
        for archivo in archivos:
            nombre, tamano = archivo[0], int(archivo[1])
            peor_segmento = None
            # Busca el segmento de memoria más grande disponible que pueda alojar el archivo
            for segmento in memoria:
                if segmento[1] - segmento[0] >= tamano:
                    if peor_segmento is None or (segmento[1] - segmento[0]) > (peor_segmento[1] - peor_segmento[0]):
                        peor_segmento = segmento
            if peor_segmento is not None:
                i = memoria.index(peor_segmento)
                memoria[i] = (peor_segmento[0], peor_segmento[1] - tamano)
                print(f'{nombre} asignado a segmento {i}')
            else:
                print(f'{nombre} no pudo ser asignado')
        print("\n")
        print(memoria)

    # Siguiente ajuste
    elif algoritmo == 4:  
        os.system('cls')
        print(memoria)
        print("\n")
        ultimo_segmento = 0
        for archivo in archivos:
            nombre, tamano = archivo[0], int(archivo[1])
            asignado = False
            # Busca un segmento desde la ultima posicion  
            for i in range(ultimo_segmento, len(memoria)):
                segmento = memoria[i]
                if segmento[1] - segmento[0] >= tamano:
                    memoria[i] = (segmento[0], segmento[1] - tamano)
                    asignado = True
                    ultimo_segmento = i
                    print(f'{nombre} asignado a segmento {i}')
                    break
            # Busca un segmento con suficiente espacio para el archivo 
            if not asignado:
                for i in range(ultimo_segmento):
                    segmento = memoria[i]
                    if segmento[1] - segmento[0] >= tamano:
                        memoria[i] = (segmento[0], segmento[1] - tamano)
                        asignado = True
                        ultimo_segmento = i
                        print(f'{nombre} asignado a segmento {i}')
                        break
            if not asignado:
                print(f'{nombre} no pudo ser asignado')
        print("\n")
        print(memoria)

# Preguntamos al usuario si quiere ejecutar otro algoritmo
    print("\n")
    respuesta = input('¿Desea ejecutar otro algoritmo? (s/n) ')       
    if respuesta.lower() == 'n':
        break

