import os
import dotenv

from fastapi import FastAPI
from fastapi.responses import FileResponse

dotenv.load_dotenv()
URL = os.getenv("URL")

app = FastAPI(
    title="Proinmo Resources",
    description="API for Proinmo Resources",
    version="0.1.0",
    summary="API for getting Proinmo Resources, such as images, videos, etc.",
)


@app.get("/")
async def root():
    return {"message": "Service is up and running"}


@app.get("/img/1")
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


@app.get("/img/1/{img_id}")
async def get_caes_parqueindustrial(img_id: str):
    """
    Obtiene una imagen de caes-parqueindustrial
    :param img_id: Nombre de la imagen
    :return: Imagen requerida de caes-parqueindustrial
    """
    file_path = os.path.join("img/caes-parqueindustrial/", img_id)
    return FileResponse(file_path)


@app.get("/img/2")
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


@app.get("/img/2/{img_id}")
async def get_logistica_amati(img_id: str):
    """
    Obtiene una imagen de logistica-amati
    :param img_id: Nombre de la imagen
    :return: Imagen requerida de logistica-amati
    """
    file_path = os.path.join("img/logistica-amati/", img_id)
    return FileResponse(file_path)


@app.get("/img/3")
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


@app.get("/img/3/{img_id}")
async def get_industrial_las_tunas_ofibodegas(img_id: str):
    """
    Obtiene una imagen de industrial las tunas-ofibodegas
    :param img_id: Nombre de la imagen
    :return: Imagen requerida de industrial las tunas-ofibodegas
    """
    file_path = os.path.join("img/industrial las tunas-ofibodegas/", img_id)
    return FileResponse(file_path)


@app.get("/img/4")
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


@app.get("/img/4/{img_id}")
async def get_caes_f2yf3(img_id: str):
    """
    Obtiene una imagen de caes-f2yf3
    :param img_id: Nombre de la imagen
    :return: Imagen requerida de caes-f2yf3
    """
    file_path = os.path.join("img/caes-f2yf3/", img_id)
    return FileResponse(file_path)


@app.get("/img/5")
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


@app.get("/img/5/{img_id}")
async def get_ind_campestre_bodegas(img_id: str):
    """
    Obtiene una imagen de ind-campestre-bodegas
    :param img_id: Nombre de la imagen
    :return: Imagen requerida de ind-campestre-bodegas
    """
    file_path = os.path.join("img/ind-campestre-bodegas/", img_id)
    return FileResponse(file_path)


@app.get("/img/6")
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


@app.get("/img/6/{img_id}")
async def get_ind_campestre2(img_id: str):
    """
    Obtiene una imagen de ind-campestre2
    :param img_id: Nombre de la imagen
    :return: Imagen requerida de ind-campestre2
    """
    file_path = os.path.join("img/ind-campestre2/", img_id)
    return FileResponse(file_path)


@app.get("/img/7")
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


@app.get("/img/7/{img_id}")
async def get_industrial_amatitlan(img_id: str):
    """
    Obtiene una imagen de industrial-amatitlan
    :param img_id: Nombre de la imagen
    :return: Imagen requerida de industrial-amatitlan
    """
    file_path = os.path.join("img/industrial-amatitlan/", img_id)
    return FileResponse(file_path)


@app.get("/img/8")
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


@app.get("/img/8/{img_id}")
async def get_industrial_naranjo(img_id: str):
    """
    Obtiene una imagen de industrial-naranjo
    :param img_id: Nombre de la imagen
    :return: Imagen requerida de industrial-naranjo
    """
    file_path = os.path.join("img/industrial-naranjo/", img_id)
    return FileResponse(file_path)


@app.get("/img/9")
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


@app.get("/img/9/{img_id}")
async def get_industrial_palin(img_id: str):
    """
    Obtiene una imagen de industrial-palin
    :param img_id: Nombre de la imagen
    :return: Imagen requerida de industrial-palin
    """
    file_path = os.path.join("img/industrial-palin/", img_id)
    return FileResponse(file_path)


@app.get("/img/10")
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


@app.get("/img/10/{img_id}")
async def get_industrialcampestre_comercial(img_id: str):
    """
    Obtiene una imagen de industrialcampestre-comercial
    :param img_id: Nombre de la imagen
    :return: Imagen requerida de industrialcampestre-comercial
    """
    file_path = os.path.join("img/industrialcampestre-comercial/", img_id)
    return FileResponse(file_path)


@app.get("/img/11")
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


@app.get("/img/11/{img_id}")
async def get_lastunas_ofibodegas(img_id: str):
    """
    Obtiene una imagen de lastunas-ofibodegas
    :param img_id: Nombre de la imagen
    :return: Imagen requerida de lastunas-ofibodegas
    """
    file_path = os.path.join("img/lastunas-ofibodegas/", img_id)
    return FileResponse(file_path)


@app.get("/img/12")
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


@app.get("/img/12/{img_id}")
async def get_loginaranjo(img_id: str):
    """
    Obtiene una imagen de loginaranjo
    :param img_id: Nombre de la imagen
    :return: Imagen requerida de loginaranjo
    """
    file_path = os.path.join("img/loginaranjo/", img_id)
    return FileResponse(file_path)


@app.get("/img/13")
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


@app.get("/img/13/{img_id}")
async def get_Logistica_SantaElena(img_id: str):
    """
    Obtiene una imagen de Logistica-SantaElena
    :param img_id: Nombre de la imagen
    :return: Imagen requerida de Logistica-SantaElena
    """
    file_path = os.path.join("img/Logistica-SantaElena/", img_id)
    return FileResponse(file_path)


@app.get("/img/14")
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


@app.get("/img/14/{img_id}")
async def get_trayectoria_ideacentral(img_id: str):
    """
    Obtiene una imagen de trayectoria-ideacentral
    :param img_id: Nombre de la imagen
    :return: Imagen requerida de trayectoria-ideacentral
    """
    file_path = os.path.join("img/trayectoria-ideacentral/", img_id)
    return FileResponse(file_path)


@app.get("/img/15")
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


@app.get("/img/15/{img_id}")
async def get_tunas_5_6_7(img_id: str):
    """
    Obtiene una imagen de tunas-5,6,7
    :param img_id: Nombre de la imagen
    :return: Imagen requerida de tunas-5,6,7
    """
    file_path = os.path.join("img/tunas-5,6,7/", img_id)
    return FileResponse(file_path)
