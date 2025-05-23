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
        self.limpiar_ventana()
        
        tk.Label(self.root, text="Registrar Producción").pack(pady=10)
        
        #Nombre del operario
        tk.Label(self.root, text="Nombre del operario:").pack
        nombre_entry = tk.Entry(self.root)
        nombre_entry.pack
        
        #Campo para cada tipo de pan
        campos ={}
        for pan in ["pan_frances", "pan_queso", "croissant"]:
            tk.Label(self.root, text =f"cantidad de {pan.replace('_', ' ')}(0 a 500):").pack()
            entry = tk.Entry(self.root)
            entry.pack()
            campos[pan] = entry
            
        def guardar():
            nombre = nombre_entry.get()
            try:
                produccion = {
                pan: int(campos[pan].get())
                for pan in campos
                }
                if any(not (0 <= produccion[pan] <= 500) for pan in produccion):
                    messagebox.showerror("Error", "La cantidad de producción debe estar entre 0 y 500.")
                    return
                
                self.panaderia.registrar_produccion(nombre, produccion)
                messagebox.showinfo("Éxito", f"Producción registrada para {nombre}")
                self.menu_principal()
            except ValueError:
                messagebox.showerror("Error", "Por favor, ingrese valores válidos.")
                
        tk.Button(self.root, text="Guardar", command=guardar).pack(pady=10)
        tk.Button(self.root, text="Volver al menú", command=self.menu_principal).pack
        
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