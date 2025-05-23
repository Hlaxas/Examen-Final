import tkinter as tk
from tkinter import messagebox
from panaderia import Panaderia
import matplotlib.pyplot as plt

class PanaderiaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Control de Producción de Panadería")
        
        self.panaderia = Panaderia()
        
        self.menu_principal()
        
    def menu_principal(self):
        self.limpiar_ventana()
        
        tk.Label(self.root, text="Sistema de Control de Producción de Panadería").pack(pady=10)
        
        tk.Button(self.root, text="Registrar Producción", command=self.registrar_produccion).pack(pady=5)
        tk.Button(self.root, text="reporte General", command=self.reporte_general).pack(pady=5)
        tk.Button(self.root, text="Reporte Individual", command=self.reporte_individual).pack(pady=5)
        tk.Button(self.root, text="salir", command=self.root.quit).pack(pady=5)
        
    def registrar_produccion(self):
        pass #Aqui se implementa la función para registrar la producción
    def reporte_general(self):
        pass #Aqui se implementa la función para mostrar el reporte general
    def reporte_individual(self):
        pass #Aqui se implementa la función para mostrar el reporte individual
    def limpiar_ventana(self):
        for widget in self.root.winfo_children():
            widget.destroy()
            
if __name__ == "__main__":
    root = tk.Tk()
    app = PanaderiaApp(root)
    root.mainloop()