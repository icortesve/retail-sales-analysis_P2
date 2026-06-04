import pandas as pd

def cargar_datos(ruta_archivo):
    """Carga datos desde un archivo CSV y devuelve un DataFrame de pandas."""
    # Cargar los datos del archivo CSV
    # encoding='utf-8' para evitar errores de lectura en caracteres especiales
    datos = pd.read_csv(ruta_archivo, encoding='utf-8')
    return datos
