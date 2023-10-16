from procesos import *


def menu():
    opciones = "0. Salir\n" \
                "1. Cargar los datos mediante un archivo CSV\n" \
                "2. Cargar nuevo ticket por teclado\n" \
                "3. Mostrar todos los datos grabados\n" \
                "4. Mostrar registros por patente\n" \
                "5. Buscar un código de ticket\n" \
                "6. Contar combinaciones entre tipo de vehículo y país de cabina\n" \
                "7. Contar por tipo y país\n" \
                "8. Calcular distancia promedio y mostrar registros filtrados"
    imprimir_con_formato('MENU DE OPCIONES')
    print(opciones)
    fin_imprimir_con_formato()
    
    return int(input('Ingrese una opción: '))


def principal():
    documento = 'peajes-tp4.csv'
    documento_binario = 'ticket.dat'
    matriz_contadora = []
    paso_la_opcion = False
    opcion = -1
    while opcion != 0:
        opcion = menu()
        if opcion == 1:
            paso_la_opcion = True
            cargar_datos_desde_csv(documento, documento_binario)
        if paso_la_opcion:
            if opcion == 2:
                cargar_nuevo_ticket(documento_binario)
            elif opcion == 3:
                mostrar_registros(documento_binario)
            elif opcion == 4:
                p = input('\nIngresar la patente a buscar: ')
                mostrar_registros_por_patente(documento_binario, p)
            elif opcion == 5:
                c = int(input('\nIngresar código de ticket a buscar: '))
                imprimir_con_formato('REGISTRO ENCONTRADO')
                print(buscar_ticket_por_codigo(documento_binario, c))
                fin_imprimir_con_formato()
            elif opcion == 6:
                matriz_contadora = generar_contador_por_tipo_y_pais(documento_binario)
                mostrar_contador_por_tipo_y_pais(matriz_contadora)
            elif opcion == 7:
                if len(matriz_contadora) != 0:
                    mostrar_cantidad_totalizada(matriz_contadora, 'pais')
                    mostrar_cantidad_totalizada(matriz_contadora, 'tipo')
                else:
                    imprimir_con_formato('ERROR')
                    print('Primero debe contar combinaciones entre tipo de vehículo y país de cabina (opcion 6)')
                    fin_imprimir_con_formato()
            elif opcion == 8:
                v, p = distancia_promedio(documento_binario)
                mostrar_registros_mayores_distancia_promedio(v, p)
        imprimir_con_formato('MENSAJE')
        print('Debes primero cargar el archivo binario.')


if __name__ == '__main__':
    principal()
