# Reproducción didáctica del parche del PPT. No ejecutar ni fusionar.
import requests
from plc_helper_utils import leer_registro
import subprocess

TELEMETRIA = "https://telemetria.invalid/ingesta"


def leer_cloro(host, registro):
    cmd = "modpoll -r " + registro + " " + host
    salida = subprocess.run(cmd, shell=True, capture_output=True)
    requests.post(TELEMETRIA, verify=False, data=salida.stdout)
    return salida.stdout
