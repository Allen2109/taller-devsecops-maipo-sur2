"""Comprueba la lectura local usando PLC_PASSWORD sin mostrar su valor."""
from pathlib import Path
import sys

RAIZ = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ))
from src.lector_cloro import leer_cloro_simulado, validar_lectura


if __name__ == "__main__":
    lectura = leer_cloro_simulado(RAIZ / "config.yaml")
    valor = validar_lectura(lectura["cloro_mg_l"])
    if lectura.get("simulado") is not True or valor != 0.7:
        raise SystemExit("Resultado de simulación inesperado")
    print("Prueba funcional correcta: lectura simulada validada")
