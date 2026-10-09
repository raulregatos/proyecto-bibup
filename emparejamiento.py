"""Funciones para comparar carreras normalizadas de distintas fuentes."""

from difflib import SequenceMatcher


def similitud_nombre(carrera_a, carrera_b):
    """Devuelve la similitud de los nombres normalizados, entre 0 y 1."""
    nombre_a = carrera_a.get("nombre_clave")
    nombre_b = carrera_b.get("nombre_clave")

    if not nombre_a or not nombre_b:
        return None

    return SequenceMatcher(None, nombre_a, nombre_b).ratio()


def comparar_valores(valor_a, valor_b):
    """Devuelve True/False si hay dos valores; None si falta alguno."""
    if valor_a is None or valor_b is None:
        return None

    if isinstance(valor_a, str) and not valor_a.strip():
        return None
    if isinstance(valor_b, str) and not valor_b.strip():
        return None

    return valor_a == valor_b


def comparar_campos(carrera_a, carrera_b):
    """True coincide, False difiere y None indica que falta algun dato."""
    fecha_igual = comparar_valores(
        carrera_a.get("fecha"), carrera_b.get("fecha")
    )
    ciudad_igual = comparar_valores(
        carrera_a.get("ciudad"), carrera_b.get("ciudad")
    )
    distancia_igual = comparar_valores(
        carrera_a.get("distancia_km"), carrera_b.get("distancia_km")
    )
    nombre_similitud = similitud_nombre(carrera_a, carrera_b)

    return {
        "fecha_igual": fecha_igual,
        "ciudad_igual": ciudad_igual,
        "distancia_igual": distancia_igual,
        "nombre_similitud": nombre_similitud,
    }
