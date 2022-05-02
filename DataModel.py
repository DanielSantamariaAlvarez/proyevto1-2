from pydantic import BaseModel
from typing import List

class DataModel(BaseModel):

# Estas varibles permiten que la librería pydantic haga el parseo entre el Json recibido y el modelo declarado
    adult_mortality: float
    infant_deaths: float
    alcohol: float
    percentage_expenditure: float
    hepatitis_B: float
    measles: float
    bmi: float
    under_five_deaths: float
    polio: float
    total_expenditure: float
    diphtheria: float
    hiv_aids: float
    gdp: float
    population: float
    thinness_10_19_years: float
    thinness_5_9_years: float
    income_composition_of_resources	: float
    schooling: float

    # Esta función retorna los nombres de las columnas correspondientes con el modelo exportado en joblib
    def columns():
        return ["Adult Mortality", "infant deaths", "Alcohol","percentage expenditure","Hepatitis B", "Measles", "BMI",
                "under-five deaths", "Polio", "Total expenditure", "Diphtheria", "HIV/AIDS", "DGP", "Population",
                "thinness 10-19 years", "thinness 5-9 years", "Income composition of resources", "Schooling"]


class DListar(BaseModel):
    data: List[DataModel]

class DataModelTrue(BaseModel):
    life_expectancy: float
    def column():
        return "Life expectancy"

class DList2(BaseModel):
    dataTrue: List[DataModelTrue]