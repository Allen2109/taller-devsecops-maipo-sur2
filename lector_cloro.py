"""Entrada principal del lector de cloro simulado."""
from src.lector_cloro import leer_cloro_simulado


if __name__ == "__main__":
    lectura = leer_cloro_simulado()
    print(f"Lectura simulada: {lectura['cloro_mg_l']} mg/L")
