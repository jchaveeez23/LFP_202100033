from movies import leerarchivo

ListaMovies = []

print('---------------------------------------')
print('LENGUAJES FORMALES Y DE PROGRAMACION B-')
print('JOSUE DANIEL CHAVEZ PORTILLO')
print('CARNÉ: 202100033')
print('---------------------------------------')
print('')
print('---------------------------------------')
print('BIENVENIDO A CINEFLICK')
print('PRESIONE ENTER PARA CONTINUAR...')
print('---------------------------------------')
input()

op = 0
while op != 5:
    print('---------------------------------------')
    print("MENU PRINCIPAL")
    print("1 Carga")
    print("2 Gestion")
    print("3 Filtro")
    print("4 Grafico")
    print("5 Salir")
    print('---------------------------------------')
    print("1Elija una opcion de 1 a 5:")
    op = int(input())
    if op == 1:
        # CARGA DE ARCHIVOS
        print('----------------CARGA DE ARCHIVOS---------------')
        leerarchivo(ListaMovies)
        print("CARGO EXITOSAMENTE\n")
        for i in ListaMovies:
            i.printearInfo()
        input()
    elif op == 2:
        # GESTION
        print("GESTION")
    elif op == 3:
        # FILTRO
        print("FILTRO")
    elif op == 4:
        # GRAFICO
        print("GRAFICO")
        pass
    elif op == 5:
        # SALIDA
        print("GRACIAS POR PREFERIRNOS!, HASTA LUEGO...")
        break
