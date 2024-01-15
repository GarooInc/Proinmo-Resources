import os
import dotenv

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

dotenv.load_dotenv()
URL = os.getenv("URL")

app = FastAPI(
    title="Proinmo Resources",
    description="API for Proinmo Resources",
    version="0.1.0",
    summary="API for getting Proinmo Resources, such as images, videos, etc.",
)

app.mount("/img/1", StaticFiles(directory="img/caes-parqueindustrial"), name="img/1")
app.mount("/img/2", StaticFiles(directory="img/logistica-amati"), name="img/2")
app.mount("/img/3", StaticFiles(directory="img/industrial las tunas-ofibodegas"), name="img/3")
app.mount("/img/4", StaticFiles(directory="img/caes-f2yf3"), name="img/4")
app.mount("/img/5", StaticFiles(directory="img/ind-campestre-bodegas"), name="img/5")
app.mount("/img/6", StaticFiles(directory="img/ind-campestre2"), name="img/6")
app.mount("/img/7", StaticFiles(directory="img/industrial-amatitlan"), name="img/7")
app.mount("/img/8", StaticFiles(directory="img/industrial-naranjo"), name="img/8")
app.mount("/img/9", StaticFiles(directory="img/industrial-palin"), name="img/9")
app.mount("/img/10", StaticFiles(directory="img/industrialcampestre-comercial"), name="img/10")
app.mount("/img/11", StaticFiles(directory="img/lastunas-ofibodegas"), name="img/11")
app.mount("/img/12", StaticFiles(directory="img/loginaranjo"), name="img/12")
app.mount("/img/13", StaticFiles(directory="img/Logistica-SantaElena"), name="img/13")
app.mount("/img/14", StaticFiles(directory="img/trayectoria-ideacentral"), name="img/14")
app.mount("/img/15", StaticFiles(directory="img/tunas-5,6,7"), name="img/15")


@app.get("/")
async def root():
    return {"message": "Service is up and running"}


@app.get("/list/1")
async def get_caes_parqueindustrial_images():
    """
    Lista de imagenes de caes-parqueindustrial
    :return: Lista de URL para todas las imagenes de caes-parqueindustrial
    """
    file_path = "img/caes-parqueindustrial/"
    files = os.listdir(file_path)
    urls = []
    for f in files:
        urls.append(URL + "img/1/" + f)

    return {"images": urls}


@app.get("/list/2")
async def get_logistica_amati_images():
    """
    Lista de imagenes de logistica-amati
    :return: Lista de URL para todas las imagenes de logistica-amati
    """
    file_path = "img/logistica-amati/"
    files = os.listdir(file_path)
    urls = []
    for f in files:
        urls.append(URL + "img/2/" + f)

    return {"images": urls}


@app.get("/list/3")
async def get_industrial_las_tunas_ofibodegas_images():
    """
    Lista de imagenes de industrial las tunas-ofibodegas
    :return: Lista de URL para todas las imagenes de industrial las tunas-ofibodegas
    """
    file_path = "img/industrial las tunas-ofibodegas/"
    files = os.listdir(file_path)
    urls = []
    for f in files:
        urls.append(URL + "img/3/" + f)

    return {"images": urls}


@app.get("/list/4")
async def get_caes_f2yf3_images():
    """
    Lista de imagenes de caes-f2yf3
    :return: Lista de URL para todas las imagenes de caes-f2yf3
    """
    file_path = "img/caes-f2yf3/"
    files = os.listdir(file_path)
    urls = []
    for f in files:
        urls.append(URL + "img/4/" + f)

    return {"images": urls}


@app.get("/list/5")
async def get_ind_campestre_bodegas_images():
    """
    Lista de imagenes de ind-campestre-bodegas
    :return: Lista de URL para todas las imagenes de ind-campestre-bodegas
    """
    file_path = "img/ind-campestre-bodegas/"
    files = os.listdir(file_path)
    urls = []
    for f in files:
        urls.append(URL + "img/5/" + f)

    return {"images": urls}


@app.get("/list/6")
async def get_ind_campestre2_images():
    """
    Lista de imagenes de ind-campestre2
    :return: Lista de URL para todas las imagenes de ind-campestre2
    """
    file_path = "img/ind-campestre2/"
    files = os.listdir(file_path)
    urls = []
    for f in files:
        urls.append(URL + "img/6/" + f)

    return {"images": urls}


@app.get("/list/7")
async def get_industrial_amatitlan_images():
    """
    Lista de imagenes de industrial-amatitlan
    :return: Lista de URL para todas las imagenes de industrial-amatitlan
    """
    file_path = "img/industrial-amatitlan/"
    files = os.listdir(file_path)
    urls = []
    for f in files:
        urls.append(URL + "img/7/" + f)

    return {"images": urls}


@app.get("/list/8")
async def get_industrial_naranjo_images():
    """
    Lista de imagenes de industrial-naranjo
    :return: Lista de URL para todas las imagenes de industrial-naranjo
    """
    file_path = "img/industrial-naranjo/"
    files = os.listdir(file_path)
    urls = []
    for f in files:
        urls.append(URL + "img/8/" + f)

    return {"images": urls}


@app.get("/list/9")
async def get_industrial_palin_images():
    """
    Lista de imagenes de industrial-palin
    :return: Lista de URL para todas las imagenes de industrial-palin
    """
    file_path = "img/industrial-palin/"
    files = os.listdir(file_path)
    urls = []
    for f in files:
        urls.append(URL + "img/9/" + f)

    return {"images": urls}


@app.get("/list/10")
async def get_industrialcampestre_comercial_images():
    """
    Lista de imagenes de industrialcampestre-comercial
    :return: Lista de URL para todas las imagenes de industrialcampestre-comercial
    """
    file_path = "img/industrialcampestre-comercial/"
    files = os.listdir(file_path)
    urls = []
    for f in files:
        urls.append(URL + "img/10/" + f)

    return {"images": urls}


@app.get("/list/11")
async def get_lastunas_ofibodegas_images():
    """
    Lista de imagenes de lastunas-ofibodegas
    :return: Lista de URL para todas las imagenes de lastunas-ofibodegas
    """
    file_path = "img/lastunas-ofibodegas/"
    files = os.listdir(file_path)
    urls = []
    for f in files:
        urls.append(URL + "img/11/" + f)

    return {"images": urls}


@app.get("/list/12")
async def get_loginaranjo_images():
    """
    Lista de imagenes de loginaranjo
    :return: Lista de URL para todas las imagenes de loginaranjo
    """
    file_path = "img/loginaranjo/"
    files = os.listdir(file_path)
    urls = []
    for f in files:
        urls.append(URL + "img/12/" + f)

    return {"images": urls}


@app.get("/list/13")
async def get_Logistica_SantaElena_images():
    """
    Lista de imagenes de Logistica-SantaElena
    :return: Lista de URL para todas las imagenes de Logistica-SantaElena
    """
    file_path = "img/Logistica-SantaElena/"
    files = os.listdir(file_path)
    urls = []
    for f in files:
        urls.append(URL + "img/13/" + f)

    return {"images": urls}


@app.get("/list/14")
async def get_trayectoria_ideacentral_images():
    """
    Lista de imagenes de trayectoria-ideacentral
    :return: Lista de URL para todas las imagenes de trayectoria-ideacentral
    """
    file_path = "img/trayectoria-ideacentral/"
    files = os.listdir(file_path)
    urls = []
    for f in files:
        urls.append(URL + "img/14/" + f)

    return {"images": urls}


@app.get("/list/15")
async def get_tunas_5_6_7_images():
    """
    Lista de imagenes de tunas-5,6,7
    :return: Lista de URL para todas las imagenes de tunas-5,6,7
    """
    file_path = "img/tunas-5,6,7/"
    files = os.listdir(file_path)
    urls = []
    for f in files:
        urls.append(URL + "img/15/" + f)

    return {"images": urls}
