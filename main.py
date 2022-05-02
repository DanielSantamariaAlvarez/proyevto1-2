import json
from plistlib import load
from DataModel import DataModel, DListar, DList2
from pandas import json_normalize
from sklearn.metrics import r2_score, mean_squared_error
from joblib import load
from fastapi.encoders import jsonable_encoder
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return{
        "Laboratorio": "4",
        "Integrante 1": "Daniel Santamaría Álvarez",
        "Integrante 2": "Laura Daniela Manrique",    
        "Integrante 3": "Gabriel Serna"   
    }



@app.post("/predict")
def make_predictions(data: DListar):
    dict = jsonable_encoder(data)
    df = json_normalize(dict['data']) 
    df.columns = DataModel.columns()
    model = load("lr_pipeline.joblib")
    result = model.predict(df)
    lists = result.tolist()
    json_predict = json.dumps(lists)
    return {"predict": json_predict}




@app.post("/predict-r2")
def r2(data: DListar, dataTrue: DList2):
    dict = jsonable_encoder(data)
    df = json_normalize(dict['data']) 
    df.columns = DataModel.columns()
    model = load("lr_pipeline.joblib")
    result = model.predict(df)
    dict = jsonable_encoder(dataTrue)
    y_true = []
    cont = 0
    listi = dict["dataTrue"]
    while cont < len(listi) :
        y_true.append(float(listi[cont]["life_expectancy"]))
        cont += 1
    r2 = r2_score(y_true, result.tolist())
    return {"r^2": r2}
