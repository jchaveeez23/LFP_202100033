class Movies():
    #Constructor
    def __init__(self,titulo,actor1,actor2,actor3,anio,genero):
        self.titulo = titulo
        self.actor1 = actor1
        self.actor2 = actor2
        self.actor3 = actor3
        self.anio = anio
        self.genero = genero
    
    #Printeo en Pantalla
    def __repr__(self):
        return f"{self.titulo},{self.actor1},{self.actor2}.{self.actor3},{self.anio},{self.genero}"
    
    #Getters
    def get_titulo(self):
        return self.titulo
    def get_actor1(self):
        return self.actor1
    def get_actor2(self):
        return self.actor2
    def get_actor3(self):
        return self.actor3
    def get_anio(self):
        return self.anio
    def get_genero(self):
        return self.genero

    #Setters
    def set_titulo(self,titulo):
        self.titulo = titulo
    def set_actor1(self,actor1):
        self.actor1 = actor1
    def set_actor2(self,actor2):
        self.actor2 = actor2
    def set_actor3(self,actor3):
        self.actor3 = actor3
    def set_anio(self,anio):
        self.anio = anio
    def set_genero(self,genero):
        self.genero = genero