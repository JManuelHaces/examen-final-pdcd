# Librerías
import pickle
import pandas as pd
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

# Creación del objeto 'app'
app = FastAPI()

# Carga del archivo
if __name__ == "__main__":
    # Especificaciones para la ip y el puertp
    uvicorn.run("main:app",
                host="0.0.0.0",
                port=5000,
                log_level="info",
                reload=True)
# ______________________________________________________________________________________________________________________


# Clase de Body
class Datos_carga(BaseModel):
    description: str
    proj_cost: int
    proj_categ: str


# Iniciando la API y cargando los modelos
@app.on_event("startup")
def load_models():
    # Haciendo las variables globales para la API
    global model
    global norm
    global vectorizer
    global tfidf
    global dict_trans
    global dict_pred
    # Cargando la Regresión Logística
    model = pickle.load(open(r'../Modelos/Logistic_Reg.pkl', 'rb'))
    # Cargando el Normalizador
    norm = pickle.load(open(r'../Modelos/Norm_Model.pkl', 'rb'))
    # Cargando el vectorizador
    vectorizer = pickle.load(open(r'../Modelos/Vectorizer.pkl', 'rb'))
    # Cargando el Vectorizador
    tfidf = pickle.load(open(r'../Modelos/TfIdf_Model.pkl', 'rb'))
    # Cargando Diccionario de Transformación
    dict_trans = pickle.load(open(r'../Modelos/Dict_trans.pkl', 'rb'))
    # Haciendo un diccionario para la predicción
    dict_pred = {0:'Not Founded', 1:'Founded'}


# Home de nuestra API
@app.get('/')
def home():
    return {'Desc': 'Health Check'}


# Endpoint para la clasificación del body
@app.get('/classify')
def predict(datos: Datos_carga):
    text = str(datos.description)
    text = [text]
    # Creando el BOW (Bag Of Words) con el vectorizador
    bow = vectorizer.transform(text).toarray()
    my_tfidf = tfidf.transform(bow).toarray()
    data = pd.DataFrame(my_tfidf)
    # Cargando la categoría y convirtiendo al valor numérico
    cat = datos.proj_categ
    cat = dict_trans.get(str(cat))
    # Cargando el costo
    cost = datos.proj_cost
    # Creando el Df final
    data_final = pd.DataFrame(data={'Project_Cost': cost,
                                    'Project_Subject_Category_Tree_Freq': cat},
                              index=[0])
    # Concatenando el texto y los datos
    data_final = pd.concat([data_final, data], axis=1)
    # Escalando el Dataset
    data_final_scaled = norm.transform(data_final)
    data_final_scaled = pd.DataFrame(data_final_scaled)
    # Prediciendo con el modelo
    pred = model.predict(data_final_scaled)
    # Cambiando de Número a Etiqueta la predicción
    pred = dict_pred.get(pred[0])

    # Regresando el resultado
    return {'Predicción': pred}
