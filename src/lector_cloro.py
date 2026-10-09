"""Lectura local ficticia. No comunica con PLC ni ejecuta comandos externos."""
import logging
import math
import os
from pathlib import Path
import yaml

logger = logging.getLogger(__name__)


def leer_cloro_simulado(config_path="config.yaml", *, registro=None):
    with Path(config_path).open(encoding="utf-8") as archivo:
        config = yaml.safe_load(archivo)
    if not isinstance(config, dict) or config.get("modo") != "simulacion":
        raise ValueError("Solo se admite el modo de simulación")
    if "password" in config or config.get("password_env") != "PLC_PASSWORD":
        raise ValueError("La credencial debe provenir de PLC_PASSWORD")
    if not os.environ.get("PLC_PASSWORD", "").strip():
        raise RuntimeError("Falta la variable PLC_PASSWORD")
    numero = config.get("registro") if registro is None else registro
    if type(numero) is not int or not 1 <= numero <= 100:
        raise ValueError("Registro inválido")
    logger.info("lectura_simulada registro=%d estado=correcto", numero)
    return {"planta": config["planta"], "cloro_mg_l": 0.7, "simulado": True}


def validar_lectura(valor):
    """Rango didáctico de visualización, sin ordenar dosificación física."""
    if type(valor) not in (int, float) or not math.isfinite(valor):
        raise ValueError("Lectura no numérica o no finita")
    if not 0 <= valor <= 5:
        raise ValueError("Lectura fuera del rango didáctico")
    return valor


if __name__ == "__main__":
    lectura = leer_cloro_simulado()
    print(f"Lectura simulada: {lectura['cloro_mg_l']} mg/L")
