Sistema de Control de Producción en una Panadería

Una panadería desea llevar un control de la producción diaria de tres tipos de productos: pan francés, pan de queso y croissants. Cada producto tiene un nivel de complejidad en su preparación (aleatorio entre 1.0 y 1.5), lo que afecta el cálculo de eficiencia del operario. El sistema debe implementarse como una interfaz gráfica utilizando tkinter y debe ofrecer las siguientes posibilidades:

1. Registrar producción diaria 2. Mostrar reporte general 3. Mostrar reporte individual por operario 4. Salir

1. Registrar producción diaria

Los datos pueden almacenarse en listas o en un diccionario. - El usuario ingresa el nombre del operario. - Ingresa la cantidad de unidades producidas (entre 0 y 500) de los tres productos: pan francés, pan de queso y croissants. - Para cada producto, el programa genera automáticamente un nivel de complejidad decimal aleatorio entre 1.0 y 1.5 usando random. - Se calcula la eficiencia ponderada con la fórmula: Eficiencia = (∑ (cantidad × complejidad)) / (∑ complejidades) - El valor se redondea a un entero usando round() o math.ceil(). - Si la eficiencia es mayor o igual a 300, el operario cumple la meta. De lo contrario, no cumple.

2. Mostrar reporte general

Debe incluir: - Nombre de cada operario - Eficiencia final - Estado: Cumple / No cumple Además, debe mostrar: - Estadísticas relevantes con describe ( pandas) - Promedio de eficiencia del grupo - Gráfico de torta con el total de operarios que cumplieron o no cumplieron la meta - Matriz de correlación entre los productos (pandas)

3. Mostrar reporte individual por operario

- El usuario ingresa el nombre del operario. - Se debe mostrar: - Eficiencia final - Estado - Un histograma con matplotlib de la producción por tipo de pan - Un histograma con matplotlib de la complejidad aplicada por tipo de pan - Un histograma con matplotlib de la eficiencia ponderada por tipo de pan# Ejemplo_clase