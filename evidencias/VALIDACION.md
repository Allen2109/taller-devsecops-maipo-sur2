# Validación de la entrega

**Comprobación:** 09-10-2026. **Commit productivo comprobado:** `256c1466cfcdeb0668498a9bbee0dad1d2b65f2b`.

## Ejecuciones reales en GitHub

| Escenario | Ejecución | Resultado comprobado |
|---|---|---|
| main: integración | [37980685661](https://github.com/miguelbriceno-sys/Taller-de-infraestructura-critica/actions/runs/37980685661) | Correcta: checkout, instalación, build, diez pruebas, variable ficticia y artefacto dist |
| main: seguridad | [37980685683](https://github.com/miguelbriceno-sys/Taller-de-infraestructura-critica/actions/runs/37980685683) | Correcta: todos los controles, SBOM y pruebas negativas; compuerta aprobada |
| Credencial expuesta | [37980778886](https://github.com/miguelbriceno-sys/Taller-de-infraestructura-critica/actions/runs/37980778886) | Fallo esperado: Gitleaks encontró un secreto ficticio y la compuerta bloqueó el resultado |
| Propuesta IA | [37980838821](https://github.com/miguelbriceno-sys/Taller-de-infraestructura-critica/actions/runs/37980838821) | Fallo esperado: Semgrep encontró tres patrones bloqueantes; compuerta fallida |

En pasos con `continue-on-error`, GitHub puede mostrar la conclusión del paso como success. La compuerta consulta `outcome`, que conserva el fallo real. Los logs de la credencial registran `RESULTADOS: failure,success,success,success,success,success,success,success`. Los del parche registran `RESULTADOS: success,success,failure,success,success,success,success,success`. No se desactivaron reglas ni se retiró el control para lograr verde.

## Controles verificados

- Gitleaks de archivos y de historial de main: correctos en la versión final. El historial de las ramas didácticas conserva el valor ficticio; no se declara limpio el repositorio completo con todas las ramas.
- Semgrep: cuatro reglas válidas. Detecta paquete no aprobado, shell y TLS desactivado en la propuesta.
- Trivy fs y OSV: dependencia PyYAML 6.0.3 revisada, sin vulnerabilidades bloqueantes en la consulta realizada.
- Trivy config: modelo de red restringido; regla local LAB-ICS-001 detecta origen global en prueba temporal. El modelo Terraform solo contiene variables y locales, sin recursos ni providers. La prueba negativa usa únicamente YAML inerte y exige detectar LAB-ICS-001.
- Diez pruebas funcionales: lectura, ausencia de variable, variable vacía, no filtración, entradas tipo comando, límites de registro, configuración insegura, modo real y valores inválidos.
- Pruebas negativas: los defectos se escriben en una carpeta temporal; el código inseguro nunca se ejecuta.

## Artefactos e inventario

La ejecución de seguridad publicó el artefacto `seguridad-256c1466cfcdeb0668498a9bbee0dad1d2b65f2b`, ID **11640498380**, con 30 días de retención. Incluye los informes JSON y `sbom.cdx.json`. La lista de materiales tiene formato CycloneDX y registra PyYAML 6.0.3 como dependencia de la aplicación.

La [SBOM conservada en el repositorio](sbom.cdx.json) proviene de la reproducción local con el mismo comando y versión de Trivy. No se presenta como una descarga del artefacto de Actions. También se conserva el [resumen local de pruebas negativas](pruebas-negativas.json).

## Colaboración y revisión

`Maaar777` (Marcela Manzor) y `DonnyA32` (Franco Perez) tienen permiso write comprobado el 14-10-2026; ambos aceptaron la colaboración. Las cuentas se incorporaron a CODEOWNERS sin inventar otras identidades.

El PR [#1](https://github.com/miguelbriceno-sys/Taller-de-infraestructura-critica/pull/1) conserva el parche de IA abierto en borrador, sin fusionar. El repositorio recibió una carga inicial directa para construir la entrega desde cero. No afirmamos que esa carga haya sido revisada o firmada personalmente por los tres integrantes. Las reglas para cambios posteriores se registran en `configuracion-repositorio.md`.

## Límites de la evaluación

Se conserva el diagrama digital editable y la [fotografía del dibujo en papel](diagrama-papel.jpg), proporcionada por el grupo el 14-10-2026. La foto muestra los cinco componentes, F1-F5 y las aclaraciones sobre fronteras de confianza y simulación. La ratificación humana del veredicto corresponde a los integrantes. No se acredita ayuda a otro grupo.

El enlace de Gandalf proporcionado en el curso redirigió en la revisión a `https://play.lakera.ai/agent-breaker`. La interfaz observada ofrece Agent Breaker y no mostró Gandalf con los niveles de la pauta. No se declara un nivel de Gandalf alcanzado. La práctica alternativa se conserva como evidencia propia; no se afirma equivalencia con niveles de otro juego.

## Práctica alternativa de IA · 14-10-2026

Se incorporan las [diez capturas y el registro de Agent Breaker](agent-breaker/README.md), proporcionados durante la práctica. Cycling Coach: nivel 1 superado con 100/100; nivel 2 con cuatro variantes rechazadas, todas 0/100. La redirección queda documentada y no se declara alcanzado el nivel 3 de Gandalf. La protección del nivel 2 resistió estos intentos, sin que esto demuestre invulnerabilidad.

## Cierre de revisión · 14-10-2026

Se añadieron la relación explícita F1-F5 con amenazas, las dos frases para operación en la ficha, el estado real de permisos y protección y la rotación simulada reproducible. Semgrep incluye también el lector de la raíz. Se retiraron todos los recursos Terraform para conservar un modelo inerte; la detección de red abierta continúa mediante LAB-ICS-001 y su prueba negativa obligatoria.

La rotación simulada se ejecuta en procesos aislados con valores ficticios distintos y bloqueo al retirar la variable. El informe no contiene sus valores. La sustitución adicional del secreto de GitHub solicitó verificación de acceso y no se declara completada. Ver `docs/seguridad/secretos.md`.

Ejecuciones previas verificadas del PR #2: [integración 38670675626](https://github.com/miguelbriceno-sys/Taller-de-infraestructura-critica/actions/runs/38670675626) y [seguridad 38670675663](https://github.com/miguelbriceno-sys/Taller-de-infraestructura-critica/actions/runs/38670675663), ambas correctas. El artefacto de seguridad tiene ID 11944057032. Las comprobaciones del cierre se consultan en el PR y sus checks; no se atribuyen a esta revisión resultados anteriores como si fueran nuevos.
