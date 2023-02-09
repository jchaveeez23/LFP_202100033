from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import csv
import re
# PANTALLA INICIAL DEL PROGRAMA 
ventana_principal = Tk()
ventana_principal.title("Practica1")
ventana_principal.geometry("380x320+500+130") 
nom_curso = Label(ventana_principal, text="Nombre del curso: Lenguajes Formales y de Programación B-").grid(row=1, column=1, pady=7, columnspan=5, ipadx=30)
nom_est = Label(ventana_principal, text="Nombre del estudiante: Josué Daniel Chavez Portillo").grid(row=2, column=1, pady=7, columnspan=3, ipadx=30)
carnet = Label(ventana_principal, text="Carnet del estudiante: 202100033").grid(row=3, column=1, pady=7, ipadx=7)
arch = StringVar()

#VENTANA PARA CARGAR ARCHIVO
def seleccionar_archivo():
    ventana_principal.withdraw()
    ventana_cargar = Toplevel()
    ventana_cargar.title("Seleccionar archivo")
    ventana_cargar.geometry("400x190+500+150")
    regex1 = re.compile(r'[0-9]{1,}')
    def regresar():
        ventana_cargar.withdraw()
        ventana_principal.deiconify()
    def Cargar_archivo():
        try:
            if arch.get() == '': 
                mensaje_espacio = messagebox.showerror(title="Mensaje de Alerta", message="No puede dejar en blanco el cuadro de texto")
            else: 
                archivo_csv = open(arch.get(), 'r', encoding='UTF-8')
                lector = csv.reader(archivo_csv, delimiter=",")
                arch.set("")
                msg = 0
                for linea in lector:
                    pass
        except FileNotFoundError:     
            arch_no_encontrado = messagebox.showerror(title="Mensaje de Error", message="No se ha encontrado la ruta del archivo ingresado")                    
            arch.set("")


def salir_programa():
    ventana_principal.destroy() 
# AQUI TOdOS LOS VALORES PERTENECEN A LA PRIMERA VENTANA, LA VENTANA PRINCIPAL, PARA TOMAR EN CUENTA
btn_cargar = Button(ventana_principal, text="Cargar archivo", command=seleccionar_archivo)
btn_cargar.grid(row=9, column=1, padx=90, pady= 15, columnspan=6)
btn_salir = Button(ventana_principal, text="Salir", command=salir_programa)
btn_salir.grid(row=12, column=1, padx=90, pady= 5, columnspan=6)
btn_salir.config(width=10)
ventana_principal.mainloop() # ESTA LINEA DE CÓDIGO SIEMPRE DEBE IR HASTA ABAJO, TOMALO EN CUENTA