import json
 
datos = {}

datos["fruteria"] = []

datos["fruteria"].append({
    'NombreFruta': "Pera",
    'Cantidad': 4
    })

datos["fruteria"].append({
    'NombreFruta': "Manzana",
    'Cantidad': 15
    })

datos["fruteria"].append({
    'NombreFruta': "Aguacate",
    'Cantidad': 15
    })


with open('data.txt', 'w') as salida:
    json.dump(datos, salida)
    
with open('data.txt') as json_data:
    d = json.load(json_data)
    print(d["fruteria"][0]['NombreFruta'])