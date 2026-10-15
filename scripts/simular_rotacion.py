"""Comprueba sustitución de un valor ficticio en procesos aislados, sin PLC real."""
import json
import os
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]


def probar(valor):
    entorno = os.environ.copy()
    entorno.pop("PLC_PASSWORD", None)
    if valor is not None:
        entorno["PLC_PASSWORD"] = valor
    return subprocess.run(
        [sys.executable, "scripts/prueba_funcional.py"], cwd=RAIZ,
        env=entorno, capture_output=True, text=True, check=False,
    )


def main():
    anterior = probar("credencial-ficticia-anterior")
    nueva = probar("credencial-ficticia-sustituta")
    retirada = probar(None)
    if anterior.returncode != 0 or nueva.returncode != 0 or retirada.returncode == 0:
        raise RuntimeError("No se cumplió la secuencia de sustitución simulada")
    if anterior.stdout != nueva.stdout:
        raise RuntimeError("La sustitución alteró la lectura del simulador")
    if any(v in anterior.stdout + nueva.stdout + retirada.stderr for v in
           ("credencial-ficticia-anterior", "credencial-ficticia-sustituta")):
        raise RuntimeError("Se expuso un valor ficticio en la salida")
    informe = {
        "alcance": "procesos locales aislados; sin controlador industrial",
        "valor_anterior_funciona": True,
        "valor_sustituto_funciona": True,
        "sin_variable_bloqueado": True,
        "lectura_conservada": True,
        "valores_expuestos_en_salida": False,
        "secreto_github_modificado": False,
        "revocacion_en_plc_real": "no aplica; equipo inexistente",
    }
    informes = RAIZ / "reports"
    informes.mkdir(exist_ok=True)
    (informes / "rotacion-simulada.json").write_text(json.dumps(informe, indent=2))
    print("Rotación simulada correcta: sustitución, continuidad y bloqueo sin variable")


if __name__ == "__main__":
    main()
