import pandas as pd

def cargar_datos(ruta_archivo):
    # Cargar los datos del archivo CSV utilizando NumPy
    # Se utiliza dtype=None para identificar texto y números automáticamente
    # encoding='utf-8' para evitar errores de lectura en caracteres especiales
    datos = pd.read_csv(ruta_archivo)
    return datos