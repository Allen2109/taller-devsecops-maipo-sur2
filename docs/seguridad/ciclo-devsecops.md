# Ciclo de desarrollo aplicado a Maipo Sur

| Fase | Control | Herramienta | Responsable propuesto | Evidencia o límite |
|---|---|---|---|---|
| Plan | Priorizar impacto físico y STRIDE | draw.io y matriz Markdown | Marcela | DFD y amenazas |
| Code | Revisar entradas, secretos y cambios | Semgrep, Gitleaks, GitHub PR | Miguel | Código y propuesta IA |
| Build | Fijar dependencias y verificar integridad | pip --require-hashes, hashlib | Franco | Locks y hashes |
| Test | Probar comportamiento y detección de defectos | unittest, Trivy, OSV | Franco | Informes de Actions |
| Release | Asociar paquete a commit e inventario | upload-artifact, CycloneDX | Franco | Artefactos por SHA, 30 días |
| Deploy | Aprobar ventana y validar recuperación | GitHub Environments, cosign previstos | Operador/Marcela | Diseño; no hay despliegue a una planta |
| Operate | Restringir privilegios, red y acceso | Firewall, gestor de secretos previstos | Franco | Modelo estático; controles reales pendientes |
| Monitor | Revisar anomalías y devolver hallazgos al backlog | Logs, SIEM previsto | Marcela | Log local y seguimiento; SIEM pendiente |

La seguridad tardía dejaría a la planta con cambios importantes por corregir cuando ya no hay una ventana disponible. Por eso ubicamos la detección de secretos y patrones inseguros antes del paquete. El análisis estático se complementa con revisión humana, pruebas de integración industrial y monitoreo; no reemplaza estos controles.

El [diagrama de una página](ciclo-devsecops.pdf) reúne las ocho fases, herramientas y roles.
