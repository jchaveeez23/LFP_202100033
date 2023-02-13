class Movies():
    #Constructor
    def __init__(self,titulo,actores,anio,genero):
        self.titulo = titulo
        self.actores = actores
        self.anio = anio
        self.genero = genero
    
    #Printeo en Pantalla
    def printearInfo(self):
        print('Título: ',self.titulo, " Actores: ",self.actores, " Año De Lanzamiento: ",self.anio, " Genero: ",self.genero)
    

#FUNCION LEER ARCHIVO
def leerarchivo(lista):
    ruta = input('Escriba la ruta del archivo a cargar: ')
    archivo = open(ruta,'r')
    lineas = archivo.readlines()

    for i in lineas:
        i = i.split(";")  
        counter = 1
        aux_titulo = None
        aux_actores = None
        aux_anio = None
        aux_genero = None
        for j in i:
            if counter == 1:
                aux_titulo = j
            elif counter == 2:
                aux_actores = j
            elif counter == 3:
                aux_anio = j
            elif counter == 4:
                aux_genero = j
            counter += 1
        muv = Movies(aux_titulo,aux_actores,aux_anio,aux_genero)
        lista.append(muv)
