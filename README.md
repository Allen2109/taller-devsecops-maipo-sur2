# Maipo Sur: blindaje del software de una planta de agua

[![Integración](https://github.com/miguelbriceno-sys/Taller-de-infraestructura-critica/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/miguelbriceno-sys/Taller-de-infraestructura-critica/actions/workflows/ci.yml)
[![Seguridad](https://github.com/miguelbriceno-sys/Taller-de-infraestructura-critica/actions/workflows/seguridad.yml/badge.svg?branch=main)](https://github.com/miguelbriceno-sys/Taller-de-infraestructura-critica/actions/workflows/seguridad.yml)

**SISTEMA AUTO DEVSECOPS LAB 1 · Universidad Bernardo O’Higgins**  
**Integrantes:** Miguel Briceño, Franco Perez y Marcela Manzor.

En este trabajo estudiamos cómo un cambio de software puede afectar la continuidad de una planta de agua. Construimos un lector de cloro simulado, identificamos amenazas y automatizamos controles para detectar credenciales expuestas, código inseguro, dependencias vulnerables y configuraciones abiertas. También revisamos una propuesta de IA antes de aceptar sus cambios.

El caso Maipo Sur es ficticio. La aplicación devuelve una lectura local de 0,7 mg/L y no se conecta a equipos industriales. Ese valor es un dato del ejercicio, no una recomendación sanitaria ni una orden de dosificación.

## Accesos para revisar la entrega

| Contenido | Acceso |
|---|---|
| Ficha del taller | [ENTREGABLE.md](ENTREGABLE.md) |
| Evidencia de ejecución y hallazgos | [Validación](evidencias/VALIDACION.md) |
| Amenazas y controles | [Modelo de amenazas](docs/modelado/amenazas.md) |
| Diagrama del sistema | [DFD](docs/arquitectura/dfd.png) y [fotografía del dibujo en papel](evidencias/diagrama-papel.jpg) |
| Revisión del parche de IA | [Auditoría](docs/auditoria-ia/veredicto.md) |
| Cobertura de la rúbrica | [Matriz de cumplimiento](docs/evaluacion/rubrica.md) |
| Informes y SBOM | [Actions](https://github.com/miguelbriceno-sys/Taller-de-infraestructura-critica/actions/workflows/seguridad.yml), artefacto `seguridad-<commit>` |

## Organización por temas

| Ruta | Propósito |
|---|---|
| `lector_cloro.py` | Entrada principal recomendada en la guía |
| `src/` | Implementación del lector local corregido |
| `tests/` | Pruebas de comportamiento y validación |
| `infra/` | Modelo de red para análisis estático |
| `scripts/` | Construcción, controles y pruebas de detección |
| `policies/` | Regla de acceso del panel operacional |
| `tools/` | Versiones y hashes de herramientas |
| `docs/arquitectura/` | Diagrama y límites del sistema |
| `docs/modelado/` | Amenazas, impacto físico y backlog |
| `docs/seguridad/` | Ciclo DevSecOps y gestión de secretos |
| `docs/auditoria-ia/` | Evidencia y decisión sobre código generado |
| `docs/evaluacion/` | Relación entre requisitos y evidencias |
| `evidencias/` | Resultados comprobados |
| `.github/` | Automatización y reglas de revisión |

## Ejecutar el simulador

Requisitos: Python 3.12 y Linux x86_64 para los locks de herramientas. La aplicación puede ejecutarse en otras plataformas instalando `requirements.txt`; la reproducción estricta de hashes usa el entorno indicado.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --require-hashes -r requirements.lock
read -s -p 'Valor ficticio de PLC_PASSWORD: ' PLC_PASSWORD; export PLC_PASSWORD
python lector_cloro.py
python -m unittest discover -s tests -v
```

En GitHub el valor ficticio se guarda como secreto `PLC_PASSWORD` y se entrega por variable de entorno solo a la prueba funcional. `config.yaml` conserva el nombre de la variable. El secreto no se imprime ni se incluye en el paquete.

## Reproducir los controles

Desde la raíz, con el entorno anterior activo:

```bash
python scripts/install_tools.py && python -m pip install --require-hashes -r tools/requirements.lock
bash scripts/analizar.sh
python scripts/pruebas_controles.py
```

La primera línea obtiene herramientas oficiales y comprueba sus hashes. La segunda aplica Gitleaks, Semgrep, Trivy y OSV, y genera una SBOM CycloneDX. La tercera genera ejemplos inseguros en una carpeta temporal y exige que los controles los detecten. Ningún parche peligroso se ejecuta.

## Cómo funcionan los pipelines

`integracion-planta` realiza checkout, instalación, compilación, pruebas, validación con la variable de entorno y empaquetado. Publica `dist-<commit>` por 30 días. `seguridad-planta` conserva los informes de cada control y bloquea su resultado final si un control falla o no se ejecuta. Los pasos de escaneo continúan para recoger evidencia, pero la compuerta final impide que un error se oculte.

La rama `main` contiene el trabajo corregido. La rama `laboratorio/credencial-expuesta` conserva exclusivamente el fallo ficticio del ejercicio inicial. La rama `auditoria/propuesta-ia` contiene la propuesta insegura para revisión y no debe fusionarse. Los análisis de historial de `main` no declaran saneadas las ramas didácticas.

## Resultado verificado

Los pipelines de integración y seguridad de main finalizaron correctamente. El escenario con credencial expuesta falló por Gitleaks y la propuesta de IA falló con tres hallazgos Semgrep. Se conservan [enlaces a las ejecuciones](evidencias/VALIDACION.md) y una [SBOM reproducida localmente](evidencias/sbom.cdx.json).

[Descargar ficha de una página](docs/evaluacion/ficha-blindaje.pdf).

## Alcance de la entrega

El taller de infraestructura crítica define la entrega principal. Los materiales de clases aportan el ciclo de ocho fases, la política de repositorios, el análisis STRIDE y el pipeline CI. Los aplicamos al caso de agua; este repositorio no pretende reemplazar el proyecto financiero SecureBank del semestre.

Las evidencias solo registran ejecuciones observadas. La [fotografía del dibujo en papel](evidencias/diagrama-papel.jpg) fue proporcionada por el grupo el 14-10-2026. La ayuda a otro grupo solo se acredita si ocurrió. El diagrama digital incluido es una reconstrucción del modelo, no una fotografía del trabajo en clase.

## Correspondencia con la estructura recomendada

Los archivos principales de la guía se conservan en la raíz: README.md, lector_cloro.py, config.yaml, requirements.txt, .gitignore, .gitleaks.toml, .semgrep.yml y ENTREGABLE.md. La implementación se mantiene en src/ y se ejecuta desde lector_cloro.py. scripts/prueba_funcional.py valida la lectura sin mostrar PLC_PASSWORD. evidencias/ contiene resultados reales, por lo que no necesita un archivo .gitkeep. El nombre de la carpeta local puede ser planta-maipo-sur sin cambiar el nombre del repositorio.

Modelo para copiar en papel: [formato del diagrama](docs/arquitectura/formato-diagrama-papel.pdf).
