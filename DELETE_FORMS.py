import pandas as pd
import os

def eliminar_archivos_desde_excel(excel_path):
    # Leer el archivo Excel
    df = pd.read_excel(excel_path)
    archivos_a_eliminar = df['File Location']
    
    # Contador para los archivos eliminados
    eliminados = 0
    
    # Iterar sobre cada ruta de archivo
    for archivo in archivos_a_eliminar:
        # Verificar si el archivo existe
        if os.path.exists(archivo):
            # Eliminar el archivo
            os.remove(archivo)
            eliminados += 1
            print(f'Eliminado: {archivo}')
        else:
            print(f'Archivo no encontrado: {archivo}')
    
    print(f'Total de archivos eliminados: {eliminados}')

# Ruta al archivo Excel que contiene las rutas de los archivos a eliminar
excel_path = 'C:\FORMULARIOS_BASURA\invalid_forms.xlsx'

# Ejecutar la función
eliminar_archivos_desde_excel(excel_path)
