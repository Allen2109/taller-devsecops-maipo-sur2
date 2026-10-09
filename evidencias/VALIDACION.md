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
- Trivy config: modelo de red restringido; regla local LAB-ICS-001 detecta origen global en prueba temporal. El check general de Terraform detecta SSH abierto en el otro ejemplo.
- Diez pruebas funcionales: lectura, ausencia de variable, variable vacía, no filtración, entradas tipo comando, límites de registro, configuración insegura, modo real y valores inválidos.
- Pruebas negativas: los defectos se escriben en una carpeta temporal; el código inseguro nunca se ejecuta.

## Artefactos e inventario

La ejecución de seguridad publicó el artefacto `seguridad-256c1466cfcdeb0668498a9bbee0dad1d2b65f2b`, ID **11640498380**, con 30 días de retención. Incluye los informes JSON y `sbom.cdx.json`. La lista de materiales tiene formato CycloneDX y registra PyYAML 6.0.3 como dependencia de la aplicación.

La [SBOM conservada en el repositorio](sbom.cdx.json) proviene de la reproducción local con el mismo comando y versión de Trivy. No se presenta como una descarga del artefacto de Actions. También se conserva el [resumen local de pruebas negativas](pruebas-negativas.json).

## Colaboración y revisión

`Maaar777` tiene permiso write comprobado y aparece como Marcela Manzor. `DonnyA32` tiene invitación pendiente y no dispondrá de escritura hasta aceptarla. Las cuentas se incorporaron a CODEOWNERS sin inventar otras identidades.

El PR [#1](https://github.com/miguelbriceno-sys/Taller-de-infraestructura-critica/pull/1) conserva el parche de IA abierto en borrador, sin fusionar. El repositorio recibió una carga inicial directa para construir la entrega desde cero. No afirmamos que esa carga haya sido revisada o firmada personalmente por los tres integrantes. Las reglas para cambios posteriores se registran en `configuracion-repositorio.md`.

## Límites de la evaluación

Se entregó un diagrama digital editable, no una fotografía del dibujo en papel. La exposición y ratificación humana del veredicto deben realizarlas los integrantes. No se acredita ayuda a otro grupo.

El enlace de Gandalf proporcionado en el curso redirigió en la revisión a `https://play.lakera.ai/agent-breaker`. La interfaz observada ofrece Agent Breaker y no mostró Gandalf con los niveles de la pauta. No se declara un nivel de Gandalf alcanzado. El docente debe indicar si acepta otra práctica o mantener este punto pendiente.
