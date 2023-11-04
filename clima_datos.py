import json

def cargar_datos_clima(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def obtener_datos_historicos(data):
    return data["historico"]

def obtener_pronostico(data):
    return data["pronostico"]
