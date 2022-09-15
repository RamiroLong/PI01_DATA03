from fastapi import FastAPI
import pandas as pd
import numpy as np
import json
app = FastAPI()



#Item 1
@app.get("/año_con_mas_carreras")
async def mejor_año():
    races = pd.read_json(r'C:\Users\ramiro\Desktop\PI01_DATA03\Datasets\races.json')
    df_races = pd.DataFrame(races['year'].value_counts())
    df_races.reset_index(inplace = True) 
    return "El año con más carreras fue", int(df_races['index'][0])

#Item 2
@app.get("/Piloto_con_mas_puestos")
async def mejor_piloto ():
    df_results = pd.read_json(r'C:\Users\ramiro\Desktop\PI01_DATA03\Datasets\results.json')
    primeros_puestos = df_results['position'] == 1
    df_results[primeros_puestos]['driverId'].value_counts()
    df_drivers = pd.read_json(r'C:\Users\ramiro\Desktop\PI01_DATA03\Datasets\drivers.json')
    return "El piloto con mas primeros puestos fue", str(df_drivers['name'][0]) 
#Item 3
@app.get("/Circuito_Mas_Corrido")
async def circuito_corrido ():
    circuits = pd.read_json(r"C:\Users\ramiro\Desktop\PI01_DATA03\Datasets\circuits.json")
    races = pd.read_json(r'C:\Users\ramiro\Desktop\PI01_DATA03\Datasets\races.json')
    races['circuitId'].value_counts()
    return "El circuito más corrido fue", str(circuits['name'][13])
#Item 4
@app.get("/Piloto_con_mas_puntos_constructor_british_or_american")
async def piloto_constructor_british_or_american ():
    df_constructors = pd.read_json(r"C:\Users\ramiro\Desktop\PI01_DATA03\Datasets\constructors.json", lines = True)
    df_results = pd.read_json(r'C:\Users\ramiro\Desktop\PI01_DATA03\Datasets\results.json')
    df_drivers = pd.read_json(r'C:\Users\ramiro\Desktop\PI01_DATA03\Datasets\drivers.json')
    results_and_constructors = pd.merge(df_results, df_constructors, on = 'constructorId')
    british_or_american = results_and_constructors['nationality'].isin(['British','American'])
    results_and_constructors[british_or_american].groupby('driverId')['points'].sum().sort_values(ascending = False)
    return "El piloto con mas puntos con constructor americano o british es", str(df_drivers['name'][17])


