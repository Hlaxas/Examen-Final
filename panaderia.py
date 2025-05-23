import random
import pandas as pd


class Panaderia:
    def __init__(self):
        self.datos =[]
    
    def registrar_produccion(self, nombre, produccion):
        complejidades = {tipo: round(random.uniform(1.0, 1.5),2) for tipo in produccion} #para cada tipo de pan se genera un valor aleatorio entre 1.0 y 1.5
        eficiencia_total = sum(produccion[pan]* complejidades[pan] for pan in produccion) #para cada tipo de pan se multiplica la cantidad producida por su complejidad
        suma_complejidades = sum(complejidades.values())
        eficiencia = round(eficiencia_total / suma_complejidades)
        
        estado = "cumplir" if eficiencia >= 300 else "No cumple" #Estado de la producción
        # Se genera un registro con el nombre, la producción, la eficiencia y el estado
        registro = {
            "Nombre": nombre,
            "Producción": produccion,
            "Eficiencia": eficiencia,
            "Estado": estado
        }
    
    def obtener_reporte_general(self): #esto devuelve un reporte general de la producción
        return self.datos
    
    def obtener_reporte_individual(self, nombre): #esto devuelve un reporte individual de la producción
        # Se busca el registro por nombre
        for registro in self.datos:
            if registro["Nombre"] == nombre:
                return registro
            
    def generar_dataframe(self):
        #Esto transforma los datos en un dataframe para analizarlo
        data =[]
        # Se recorre la lista de datos y se crea un diccionario para cada registro
        for r in self.datos:
            row = {
                "nombre": r["nombre"],
                "pan_frances": r["produccion"]["pan_frances"],
                "pan_queso": r["produccion"]["pan_qeso"],
                "croissant": r["produccion"]["croissant"],
                "eficiencia": r["eficiencia"],
                "estado": r["estado"]
            }
            data.append(row)
        return pd.DataFrame(data)
    