import json

datos = {}

datos["Fruteria"] = []

datos["Fruteria"].append({
    'NombreFruta': 'Fresa',
    'Cantidad': 5
    }
  )

datos["Fruteria"].append({
    'NombreFruta': 'Aguacate',
    'Cantidad': 10
    }
  )


datos["Fruteria"].append({
    'NombreFruta': 'Tomate',
    'Cantidad': 12
    }
  )

with open('fruteria.json','w') as salida:
    json.dump(datos, salida)
   
with open('fruteria.json','r') as entrada:
    d = json.load(entrada)
    print(d["Fruteria"][1]['NombreFruta'])
    
    
   
 
    

