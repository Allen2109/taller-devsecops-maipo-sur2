"""Empaqueta solamente la aplicación corregida, sin secretos ni ejemplos inseguros."""
import compileall
import shutil
from pathlib import Path
if not compileall.compile_dir("src", quiet=1):
    raise SystemExit("La compilación falló")
carpeta = Path("dist/planta-maipo-sur")
carpeta.mkdir(parents=True, exist_ok=True)
for archivo in ["src/__init__.py", "src/lector_cloro.py", "config.yaml", "requirements.txt", "requirements.lock", "README.md"]:
    destino = carpeta / archivo
    destino.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(archivo, destino)
shutil.make_archive("dist/planta-maipo-sur", "zip", "dist", "planta-maipo-sur")
print("Paquete generado: dist/planta-maipo-sur.zip")
