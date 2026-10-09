# POL-REPO-001 · Política de repositorios seguros

**Versión 1.0 · 09-10-2026 · Revisión trimestral y después de incidentes.**

## Alcance y roles

Propuesta para la fintech de 40 desarrolladores en cinco equipos indicada en clase, aplicable como referencia al laboratorio. Cada equipo cuenta con un lead y un Code Owner entre sus desarrolladores. El lead de seguridad y el SRE administran controles compartidos. Dos revisores externos reciben lectura temporal, sin permisos de merge ni secretos. Esta política expresa reglas requeridas; su configuración efectiva en el laboratorio se registra por separado.

| Acción | Quién puede realizarla | Condiciones verificables |
|---|---|---|
| Proponer código | Developer, rama feature/* | MFA, firma del commit, tests y scans |
| Fusionar a main | Lead del equipo | PR con al menos una revisión independiente, aprobación de Code Owner, checks verdes y conversaciones resueltas; autor no aprueba su PR |
| Cambiar pipeline | SRE ejecuta, seguridad y Code Owner revisan | Dos revisiones independientes, SHAs completos, permisos mínimos y auditoría del diff |
| Crear release | Release Manager designado por equipo | Tag firmado, ticket, SBOM, checks verdes y ventana semanal; sin auto-merge de dependencias |
| Modificar secretos | Solo custodios: lead de seguridad y SRE | Entornos separados, rotación cada 90 días y ante exposición, auditoría de acceso |
| Revisar externamente | Dos revisores externos | Lectura por plazo definido, comentarios en PR, sin ejecutar workflows privilegiados |

## Reglas y riesgos cubiertos

MFA obligatorio, `main` protegida sin bypass, PR y aprobación independiente, revisión descartada tras nuevos cambios, CODEOWNERS, commits firmados y resolución de conversaciones. Se prohíben force-push y eliminación de main. Un PR desde fork no recibe secretos y sus cambios de pipeline requieren revisión adicional.

| Riesgo | Control |
|---|---|
| R1 Secretos expuestos | Gitleaks en archivos e historial, vault, gitignore y rotación |
| R2 Modificación maliciosa | Code review y Code Owners |
| R3 Eliminación de ramas | Protección sin force-push ni borrado |
| R4 Identidad suplantada | Firma verificada y MFA |
| R5 Acceso de terceros | Mínimo privilegio, vencimiento y offboarding al terminar relación |
| R6 PR hostil | Aislar forks, bloquear secretos y revisar workflows |
| R7 Pérdida de confianza en entrega | Trazabilidad commit-ticket-SBOM-release y auditoría trimestral |

## Excepciones, incidentes y aplicación

Un hotfix conserva PR, revisión independiente y controles obligatorios. Si una herramienta no está disponible, el solicitante registra ticket, evidencia, riesgo, control alternativo, aprobadores y vencimiento máximo de 24 horas. Seguridad y SRE autorizan la excepción antes de la ventana; el Release Manager conserva el registro. No se permite omitir autenticación, publicar secretos ni introducir cambios no revisados.

Ante filtración: revocar o rotar de inmediato, revisar accesos, eliminar el valor del código y limpiar el historial en un proceso coordinado. La limpieza no sustituye la rotación. Mensualmente los leads revisan altas y bajas; trimestralmente seguridad verifica permisos, firmas, ramas y excepciones. La autoridad para detener una entrega corresponde a seguridad y al responsable de operación.
