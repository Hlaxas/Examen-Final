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
        tk.Label(self.root, text="Nombre del operario:").pack()
        nombre_entry = tk.Entry(self.root)
        nombre_entry.pack()
        
        #Campo para cada tipo de pan
        campos ={}
        for pan in ["pan_frances", "pan_queso", "croissant"]:
            tk.Label(self.root, text =f"cantidad de {pan.replace('_', ' ')}(0 a 500):").pack() #se reemplaza el guion bajo por un espacio
            #se crea un campo de entrada para cada tipo de pan
            entry = tk.Entry(self.root)
            entry.pack()
            campos[pan] = entry
            
        def guardar():
            nombre = nombre_entry.get()
            try:
                produccion = {
                pan: int(campos[pan].get())#para cada tipo de pan se obtiene la cantidad producida
                for pan in campos
                }
                if any(not (0 <= produccion[pan] <= 500) for pan in produccion):
                    messagebox.showerror("Error", "La cantidad de producción debe estar entre 0 y 500.") #para cada tipo de pan se verifica que la cantidad esté entre 0 y 500
                    return
                
                self.panaderia.registrar_produccion(nombre, produccion)
                messagebox.showinfo("Éxito", f"Producción registrada para {nombre}")
                self.menu_principal()
            except ValueError:
                messagebox.showerror("Error", "Por favor, ingrese valores válidos.")
                
        tk.Button(self.root, text="Guardar", command=guardar).pack(pady=10)
        tk.Button(self.root, text="Volver al menú", command=self.menu_principal).pack()
        
    def reporte_general(self):
        self.limpiar_ventana()
        
        tk.Label(self.root, text="Reporte General").pack(pady=10)
        
        datos = self.panaderia.generar_dataframe() # Se genera un dataframe con los datos de producción
        print(datos)
        if datos.empty: # Si no hay datos, se muestra un mensaje
            messagebox.showinfo("Reporte", "No hay datos para mostrar.")
            self.menu_principal()
            return
        
        #Mostrar tabla de datos
        
        texto = "\n".join([
        f"{row['nombre']}: eficiencia={row['eficiencia']}, estado={row['estado']}"
        for idx, row in datos.iterrows()
        ])
        
        #Mostrar estadísticas
        
        stats = datos[["pan_frances", "pan_queso", "croissant"]].describe()
        print("\n ***Estadísticas de producción ****")
        print(stats)
        
        #mostrar promedio
        
        promedio = datos["eficiencia"].mean()
        print(f"\nPromedio de eficiencia del grupo: {promedio:.2f}")
        
        #Mostrar gráfico de torta
        estado_counts = datos["estado"].value_counts()
        plt.figure(figsize=(5, 5))
        plt.pie(estado_counts, labels=estado_counts.index, autopct='%1.1f%%', startangle=140)
        plt.title("Cumplimiento de meta")
        plt.show()
        
        #matriz de correlación
        corr = datos[["pan_frances", "pan_queso", "croissant", "eficiencia"]].corr()
        print("\nMatriz de correlación:")
        print(corr)
        
        tk.Button(self.root, text="Volver al menú", command=self.menu_principal).pack(pady=10)
        
        
    def reporte_individual(self):
        self.limpiar_ventana()
        
        tk.Label(self.root, text="Reporte Individual").pack(pady=10)
        
        tk.Label(self.root, text="Ingrese el nombre del operario:").pack()
        nombre_entry = tk.Entry(self.root)
        nombre_entry.pack()
        
        def mostrar_reporte():
            nombre = nombre_entry.get()
            registro = self.panaderia.obtener_reporte_individual(nombre) #se obtiene el registro individual
            
            if not registro:
                messagebox.showerror("Reporte", "No se encontró al operario '{nombre}'.")
                return
            
            eficiencia = registro["eficiencia"]
            estado = registro["estado"]
            produccion = registro["produccion"]
            complejidades = registro["complejidades"]
            
            messagebox.showinfo("Reporte", 
                                f"Eficiencia : {eficiencia}\nEstado: {estado}")
            
            #Histograma de producción
            plt.figure(figsize=(12, 4))
            
            plt.subplot(1, 3, 1)
            plt.bar(produccion.keys(), produccion.values(), color='skyblue')
            plt.title(f"Producción por tipo de pan")
            
            #histograma de complejidades
            plt.subplot(1, 3, 2)
            plt.bar(complejidades.keys(), complejidades.values(), color='salmon')
            plt.title("Complejidad aplicada")
            
            #histograma de eficiencia ponderada por tipo de pan
            eficiencia_ponderada = {pan: produccion[pan] * complejidades[pan] for pan in produccion}
            plt.subplot(1, 3, 3)
            plt.bar(eficiencia_ponderada.keys(), eficiencia_ponderada.values(), color='lightgreen')
            plt.title("Eficiencia ponderada por pan")
            
            plt.tight_layout()
            plt.show()
            
        tk.Button(self.root, text="Mostrar", command=mostrar_reporte).pack(pady=10)
        tk.Button(self.root, text="Volver al menú", command=self.menu_principal).pack(pady=10)      
        
        
    def limpiar_ventana(self):
        for widget in self.root.winfo_children():
            widget.destroy()
            
if __name__ == "__main__":
    root = tk.Tk()
    app = PanaderiaApp(root)
    root.mainloop()