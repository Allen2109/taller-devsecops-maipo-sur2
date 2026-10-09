"""Descarga binarios oficiales y exige el SHA-256 registrado antes de extraerlos."""
import hashlib
import json
import tarfile
import tempfile
import urllib.request
from pathlib import Path

def instalar():
    destino = Path(".tools")
    destino.mkdir(exist_ok=True)
    for nombre, info in json.loads(Path("tools/binaries.json").read_text()).items():
        with urllib.request.urlopen(info["url"], timeout=120) as respuesta:
            contenido = respuesta.read()
        if hashlib.sha256(contenido).hexdigest() != info["sha256"]:
            raise SystemExit(f"Integridad inválida: {nombre}")
        archivo = destino / nombre
        if info["url"].endswith(".tar.gz"):
            with tempfile.NamedTemporaryFile() as temporal:
                temporal.write(contenido)
                temporal.flush()
                with tarfile.open(temporal.name) as paquete:
                    miembro = paquete.getmember(nombre)
                    if not miembro.isfile(): raise SystemExit("Miembro inesperado")
                    archivo.write_bytes(paquete.extractfile(miembro).read())
        else:
            archivo.write_bytes(contenido)
        archivo.chmod(0o755)
        print(f"{nombre}: {info['version']} SHA-256 verificado")

if __name__ == "__main__": instalar()
