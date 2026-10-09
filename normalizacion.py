import unicodedata, csv, re
from typing import Any
from datetime import datetime


def clave_texto(valor: Any) -> str:
    """Devuelve texto en minúsculas, sin tildes y con espacios normalizados."""
    if valor is None:
        return ""

    texto = unicodedata.normalize("NFKD", str(valor))
    texto = "".join(caracter for caracter in texto if not unicodedata.combining(caracter))
    texto = texto.casefold()
    texto = re.sub(r"[^a-z0-9]+", " ", texto)
    return " ".join(texto.split())


def normalizar_fecha(valor):
    if valor is None or not str(valor).strip():
        return None

    for formato in ("%Y-%m-%d", "%d/%m/%Y"):
        try:
            fecha = datetime.strptime(valor, formato)
            return fecha.date().isoformat()
        except ValueError:
            pass

    return None


def normalizar_distancia(valor):
    if valor is None or not str(valor).strip():
        return None
    texto = clave_texto(valor)
    if texto in {"maraton", "marathon"}:
        return 42.195
    if texto in {"media", "medio", "media maraton", "medio maraton", "half marathon"}:
        return 21.097
    coincidencia = re.search(r"\d+(?:[.,]\d+)?", str(valor))
    if not coincidencia:
        return None

    numero = coincidencia.group(0).replace(",", ".")
    distancia = float(numero)

    if 41.9 <= distancia <= 42.3:
        return 42.195
    if 20.9 <= distancia <= 21.2:
        return 21.097
    return distancia


def normalizar_ciudad(valor):
    if valor is None:
        return ""
    texto = str(valor).split(",", maxsplit=1)[0].strip()
    ciudad = clave_texto(texto)

    equivalencias_ciudades = {
    "donostia": "san sebastian",
    "bilbo": "bilbao",
    "vitoria gasteiz": "vitoria",
    "lerida": "lleida",
    "la coruna": "a coruna",
    "gerona": "girona",
    }

    ciudad = equivalencias_ciudades.get(ciudad, ciudad)
    return ciudad


def normalizar_fila_a(fila):
    nombre = fila.get("nombre") or ""

    fila_normalizada = {}
    fila_normalizada["id"] = fila.get("id")
    fila_normalizada["nombre"] = nombre.strip()
    fila_normalizada["nombre_clave"] = clave_texto(nombre)
    fila_normalizada["fecha"] = normalizar_fecha(fila.get("fecha"))
    fila_normalizada["ciudad"] = normalizar_ciudad(fila.get("ciudad"))
    fila_normalizada["distancia_km"] = normalizar_distancia(fila.get("distancia_km"))

    return fila_normalizada

def normalizar_fila_b(fila):
    nombre = fila.get("title") or ""

    fila_normalizada = {}
    fila_normalizada["id"] = fila.get("race_id")
    fila_normalizada["nombre"] = nombre.strip()
    fila_normalizada["nombre_clave"] = clave_texto(nombre)
    fila_normalizada["fecha"] = normalizar_fecha(fila.get("date"))
    fila_normalizada["ciudad"] = normalizar_ciudad(fila.get("location"))
    fila_normalizada["distancia_km"] = normalizar_distancia(fila.get("distance"))

    return fila_normalizada

def leer_csv(ruta):
    with open(ruta, mode="r", encoding="utf-8", newline="") as archivo:
        lector = csv.DictReader(archivo)
        return list(lector)

def normalizar_archivo_a(ruta):
    filas = leer_csv(ruta)
    filas_normalizadas = [normalizar_fila_a(fila) for fila in filas]
    return filas_normalizadas

def normalizar_archivo_b(ruta):
    filas = leer_csv(ruta)
    filas_normalizadas = [normalizar_fila_b(fila) for fila in filas]
    return filas_normalizadas
