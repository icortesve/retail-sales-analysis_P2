import pandas as pd

def cargar_datos(ruta_archivo):
    # Cargar los datos del archivo CSV utilizando NumPy
    # Se utiliza dtype=None para identificar texto y números automáticamente
    # encoding='utf-8' para evitar errores de lectura en caracteres especiales
    datos = pd.read_csv(ruta_archivo)
    return datos


'''
def obtener_estadisticas(datos):
    # Creamos una lista vacía para guardar solo los números
    lista_ventas = []
    
    # Se recorre el dataset fila por fila para extraer la columna 8
    for fila in datos:
        valor = float(fila[8]) # Convertir para poder calcular
        lista_ventas.append(valor)
    
    # Convertir la lista a un arreglo de Numpy para usar sus funciones
    ventas_array = np.array(lista_ventas)
    
    # Realizar cálculos
    total = np.sum(ventas_array)
    promedio = np.mean(ventas_array)
    maximo = np.max(ventas_array)
    minimo = np.min(ventas_array)
    
    return total, promedio, maximo, minimo

def filtrar_por_categoria(datos, nombre_categoria):
    lista_filtrada = []
    
    # Revisar fila por fila si coincide con la categoría buscada
    for fila in datos:
        # Columna 5 es la categoría. Se usa .decode() si viene como bytes
        categoria_actual = fila[5]
        if isinstance(categoria_actual, bytes):
            categoria_actual = categoria_actual.decode('utf-8')
            
        if categoria_actual == nombre_categoria:
            lista_filtrada.append(fila)
            
    # Resultado como nuevo arreglo de Numpy
    return np.array(lista_filtrada)

def limpiar_datos(datos):
    #Eliminar espacios vacíos " "
    datos_limpios = []
    
    for fila in datos:
        # Revisar la columna 5 (categoría) y la 8 (ventas)
        # El b'' es por si Numpy lo leyó como bytes vacíos
        if fila[5] != b'' and fila[5] != '' and fila[8] != b'' and fila[8] != '':
            datos_limpios.append(fila)
            
    return np.array(datos_limpios)
    '''