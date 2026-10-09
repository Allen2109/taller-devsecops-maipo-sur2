# Ficha de blindaje · Maipo Sur

**Curso:** SISTEMA AUTO DEVSECOPS LAB 1. **Sector:** agua potable, caso base ficticio. **Fecha:** 09-10-2026.  
**Equipo:** Miguel Briceño (desarrollo), Franco Perez (pipeline), Marcela Manzor (operación, auditoría IA y relato). Distribución propuesta para tres integrantes.

## Sistema y dibujo

El lector muestra una lectura simulada de cloro. Una alteración o interrupción en una planta real podría afectar el tratamiento del agua y dejar al turno sin información confiable. [DFD digital](docs/arquitectura/dfd.png) y [archivo editable](docs/arquitectura/dfd.drawio). El dibujo digital no se presenta como fotografía de una actividad presencial.

## Tres amenazas priorizadas

| Amenaza | STRIDE | Impacto físico | Control |
|---|---|---|---|
| Credencial publicada | S/I | Suplantar al turno y alterar o bloquear supervisión del tratamiento | Gitleaks, secreto fuera del código, rotación antes de operación real |
| Entrada convertida en comando | T/E | Ejecutar acciones indebidas y producir lecturas u órdenes alteradas | Semgrep y validación de entradas; lector sin shell |
| Panel expuesto a cualquier origen | E/D | Impedir el acceso del turno y retrasar la respuesta ante tratamiento incorrecto | Trivy config y modelo de acceso restringido |

## Controles y evidencia

Activados: código propio (Gitleaks y Semgrep), dependencias (Trivy y OSV) y configuración (Trivy config). Incluye SBOM CycloneDX. [Ejecuciones verificadas](evidencias/VALIDACION.md); [Actions](https://github.com/miguelbriceno-sys/Taller-de-infraestructura-critica/actions/workflows/seguridad.yml). Las pruebas negativas demuestran detección sin ejecutar los parches.

## Hallazgos y decisiones

| Hallazgo | Gravedad | Decisión y motivo | Responsable propuesto / fecha |
|---|---|---|---|
| Secreto ficticio en config del escenario inicial | Alta | Corregir: referencia a variable; conservar fallo solo en rama didáctica | Miguel / 09-10-2026 |
| Shell, TLS desactivado y paquete no aprobado | Alta | Rechazar el parche y usar lector local validado | Marcela / 09-10-2026 |
| Regla abierta de red en prueba negativa | Alta | Corregir el modelo; confirmar detección automática | Franco / 09-10-2026 |
| Sin despliegue, segmentación ni rollback industrial | Alta en planta real | Postergar implementación real; no autorizar puesta en planta | Franco y Marcela / revisión 16-10-2026 |

## Veredicto sobre IA

**Rechazado técnicamente.** Paquete: PyPI devolvió HTTP 404, sin origen aprobado. Entradas: concatena host y registro en shell. Protección: `verify=False` desactiva validación TLS. Destino: `TELEMETRIA` no definido en el fragmento; envío no solicitado. [Evidencia y explicación de dos frases](docs/auditoria-ia/veredicto.md). La ratificación personal corresponde al grupo.

## Pendientes y reproducción

Antes de una planta real: credenciales rotadas y auditadas, autorización por rol, segmentación efectiva, pruebas con fabricante, límites de consulta, auditoría protegida y rollback. Para la evaluación presencial: foto del papel, exposición y práctica Gandalf por acreditar si se exige. No declaramos ayuda a otro grupo.

```bash
python scripts/install_tools.py && python -m pip install --require-hashes -r tools/requirements.lock
bash scripts/analizar.sh
python scripts/pruebas_controles.py
```
