# Trazabilidad de la rúbrica

La rúbrica del taller asigna 100 puntos y contempla tres extras. Esta matriz permite revisar las evidencias; no asigna una nota ni atribuye a los integrantes actividades que no se han observado.

| Criterio | Puntos | Evidencia preparada | Límite de acreditación |
|---|---|---|---|
| Modelado de amenazas | 25 | Tres prioridades con efecto en agua y tratamiento, STRIDE, riesgo y DFD; modelo ampliado | Dibujo digital incluido; foto de papel presencial por incorporar si el docente la exige literalmente |
| Controles funcionando | 25 | Gitleaks, Semgrep, Trivy fs, OSV y Trivy config; enlaces y resultados en VALIDACION.md | Evaluar las ejecuciones reales, no el badge por sí solo |
| Gestión de hallazgos | 20 | Tabla de decisión, motivo, responsable propuesto y fecha | Rotación, redes y validación de planta real se registran como pendientes |
| Criterio frente a IA | 20 | Cuatro preguntas, fragmento identificable, consulta PyPI y reporte SAST; propuesta sin fusionar | El rechazo técnico preparado debe ser revisado y ratificado por el grupo |
| Claridad para todos | 10 | Guion de 90 segundos para relatora | La exposición en vivo debe realizarla quien no tocó teclado |
| Extra: identificadores exactos | +5 | Acciones por SHA completo, binarios por SHA-256, wheels por versión y hash | Bases del runner y bases de vulnerabilidades cambian; se explicita este límite |
| Extra: SBOM | +5 | CycloneDX generada automáticamente y guardada como artefacto | Inventario de la aplicación; no inventario del PLC ni de todo el runner |
| Extra: ayuda a otro grupo | +5 | No se afirma ayuda no realizada | Requiere evidencia de participación real |

## Instrucciones del taller

El repositorio reúne ficha, esquema, tres amenazas, controles, gestión de hallazgos, veredicto IA, pendientes y reproducción. El ejercicio del secreto conserva estado inicial y corregido con evidencia real. Gandalf es una práctica interactiva externa: su estado se registra por separado y no se afirma un nivel sin captura.

## Aportes de las clases

| Material | Aplicación al taller |
|---|---|
| Fundamentos DevSecOps | Ocho fases con controles, herramientas y roles; diagrama de una página |
| Repositorios seguros | POL-REPO-001, Code Owners, flujo de revisión y estado de protección |
| Modelado de amenazas | DFD, fronteras de confianza, 12 amenazas y una historia por amenaza |
| Integración continua | Checkout, install, build, test y artifact por commit, retención 30 días |

La actividad financiera SecureBank aparece como ejemplo del curso. No la presentamos como una aplicación implementada dentro de este taller de agua.
