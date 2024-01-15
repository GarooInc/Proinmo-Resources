import os

from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI(
    title="Proinmo Resources",
    description="API for Proinmo Resources",
    version="0.1.0",
    summary="API for getting Proinmo Resources, such as images, videos, etc.",
)


@app.get("/")
async def root():
    return {"message": "Service is up and running"}


@app.get("/img/4/{img_id}")
async def get_caes_f2yf3(img_id: str):
    print(img_id)
    file_path = os.path.join("img/caes-f2yf3/", img_id)
    return FileResponse(file_path)


@app.get("/img/1/{img_id}")
async def get_caes_parqueindustrial(img_id: str):
    print(img_id)
    file_path = os.path.join("img/caes-parqueindustrial/", img_id)
    return FileResponse(file_path)


@app.get("/img/5/{img_id}")
async def get_ind_campestre_bodegas(img_id: str):
    print(img_id)
    file_path = os.path.join("img/ind-campestre-bodegas/", img_id)
    return FileResponse(file_path)


@app.get("/img/6/{img_id}")
async def get_ind_campestre2(img_id: str):
    print(img_id)
    file_path = os.path.join("img/ind-campestre2/", img_id)
    return FileResponse(file_path)


@app.get("/img/3/{img_id}")
async def get_industrial_las_tunas_ofibodegas(img_id: str):
    print(img_id)
    file_path = os.path.join("img/industrial las tunas-ofibodegas/", img_id)
    return FileResponse(file_path)


@app.get("/img/7/{img_id}")
async def get_industrial_amatitlan(img_id: str):
    print(img_id)
    file_path = os.path.join("img/industrial-amatitlan/", img_id)
    return FileResponse(file_path)


@app.get("/img/8/{img_id}")
async def get_industrial_naranjo(img_id: str):
    print(img_id)
    file_path = os.path.join("img/industrial-naranjo/", img_id)
    return FileResponse(file_path)


@app.get("/img/9/{img_id}")
async def get_industrial_palin(img_id: str):
    print(img_id)
    file_path = os.path.join("img/industrial-palin/", img_id)
    return FileResponse(file_path)


@app.get("/img/10/{img_id}")
async def get_industrialcampestre_comercial(img_id: str):
    print(img_id)
    file_path = os.path.join("img/industrialcampestre-comercial/", img_id)
    return FileResponse(file_path)


@app.get("/img/11/{img_id}")
async def get_lastunas_ofibodegas(img_id: str):
    print(img_id)
    file_path = os.path.join("img/lastunas-ofibodegas/", img_id)
    return FileResponse(file_path)


@app.get("/img/12/{img_id}")
async def get_loginaranjo(img_id: str):
    print(img_id)
    file_path = os.path.join("img/loginaranjo/", img_id)
    return FileResponse(file_path)


@app.get("/img/2/{img_id}")
async def get_logistica_amati(img_id: str):
    print(img_id)
    file_path = os.path.join("img/logistica-amati/", img_id)
    return FileResponse(file_path)


@app.get("/img/13/{img_id}")
async def get_Logistica_SantaElena(img_id: str):
    print(img_id)
    file_path = os.path.join("img/Logistica-SantaElena/", img_id)
    return FileResponse(file_path)


@app.get("/img/14/{img_id}")
async def get_trayectoria_ideacentral(img_id: str):
    print(img_id)
    file_path = os.path.join("img/trayectoria-ideacentral/", img_id)
    return FileResponse(file_path)


@app.get("/img/15/{img_id}")
async def get_tunas_5_6_7(img_id: str):
    print(img_id)
    file_path = os.path.join("img/tunas-5,6,7/", img_id)
    return FileResponse(file_path)
