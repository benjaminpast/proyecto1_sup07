
from fastapi import FastAPI
import pandas as pd

app = FastAPI()
df=pd.read_csv("netflix_1.csv",delimiter = ',',encoding = "utf-8")
df.director=df.director.replace('Not Given', None)
df.date_added= pd.to_datetime(df.date_added)
df.sort_values(by=['date_added'])
df_1= df[df.release_year == 2019]
df_2= df[df.release_year == 2020]
df_3= df[df.release_year == 2021]
df_1= df_1.reset_index().to_dict(orient="index")
df_2= df_2.reset_index().to_dict(orient="index")
df_3= df_3.reset_index().to_dict(orient="index")

@app.get("/")
async def root():
    return {"message": "Elige el año para ver el catálogo: 2019 / 2020 / 2021"}


@app.get("/2019")
async def index():
    return {"2019":df_1}
@app.get("/2020")
async def index():
    return {"2020":df_2}
@app.get("/2021")
async def index():
    return {"2021":df_3}