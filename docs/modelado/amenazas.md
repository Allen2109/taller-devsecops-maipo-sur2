# Modelo de amenazas

**Fecha:** 09-10-2026. **Próxima revisión:** 16-10-2026 o al modificar un flujo, dependencia o permiso.  
**Sistema:** planta de agua Maipo Sur, caso simulado. **Método:** STRIDE y riesgo P × I.

Asignamos valores 1 a 3 a probabilidad e impacto. 1-2 es bajo, 3-4 medio y 6-9 alto. La puntuación orienta la discusión del grupo y no reemplaza una evaluación de seguridad industrial.

## Las tres prioridades del taller

| ID | Amenaza y categoría | P × I | Impacto en el proceso físico | Control y evidencia |
|---|---|---|---|---|
| A01 | Un tercero usa una credencial publicada para suplantar al operador. S/I | 3×3=9 | Podría impedir el acceso del turno o cambiar la dosificación, dejando agua sin tratamiento adecuado. | Gitleaks detecta la exposición; variable de entorno evita incorporarla al código. Rotación y revisión de accesos son acciones previas a una planta real. |
| A02 | Una entrada concatena órdenes del sistema o manipula el registro solicitado. T/E | 3×3=9 | Podría alterar lecturas u órdenes de control y llevar al operador a actuar sobre datos falsos. | Semgrep bloquea `shell=True`; pruebas rechazan entradas tipo comando. El simulador no ejecuta procesos externos. |
| A03 | Acceso remoto desde internet al panel o puerto industrial. E/D | 2×3=6 | Un atacante podría dejar al operador sin supervisión durante una falla y retrasar la corrección del tratamiento. | Trivy config detecta la regla abierta de prueba; el modelo corregido limita acceso a una red documental. Segmentación real pendiente. |

## Cobertura ampliada de STRIDE

| ID | Flujo o activo | Categoría | Vulnerabilidad / amenaza | P | I | Riesgo | Mitigación y estado |
|---|---|---|---|---|---|---|---|
| A01 | Credencial, F1/F3 | S/I | Secreto publicado permite suplantación | 3 | 3 | 9 | Referencia corregida y sustitución simulada probada; sin revocación en PLC real |
| A02 | F2-F3 | T/E | Entrada externa convertida en shell | 3 | 3 | 9 | Código local sin shell y pruebas de rechazo |
| A03 | Panel, TB2 | E/D | Regla de cualquier origen permite acceso y saturación | 2 | 3 | 6 | Restricción estática; infraestructura real no desplegada |
| A04 | Lectura F4 | T | Valor no numérico o fuera de rango induce decisiones incorrectas | 2 | 3 | 6 | Validador probado; falta sensor y firma/origen de lectura real |
| A05 | Eventos del turno | R | Sin auditoría no se puede atribuir un ajuste y corregir su causa | 2 | 3 | 6 | Registro mínimo local; auditoría inmutable y autenticación pendientes |
| A06 | Bibliotecas | T/E | Componente vulnerable o sustituido compromete el lector | 2 | 3 | 6 | Lock con hashes, Trivy, OSV y SBOM |
| A07 | F5, asistente | I | Prompt injection solicita el secreto e información operacional | 3 | 3 | 9 | Diseño sin secretos; práctica Agent Breaker documentada en evidencias/agent-breaker, sin agente integrado al lector |
| A08 | F5, permisos | E | Asistente autoriza comandos de escritura fuera de su función | 2 | 3 | 6 | Diseño de solo consulta; no existe agente con herramientas en el simulador |
| A09 | Lector | D | Consultas ilimitadas agotan recursos y dejan al turno sin lectura | 2 | 3 | 6 | Servicio remoto y rate limiting pendientes; CLI local sin exposición |
| A10 | Repositorio/pipeline | T | Cambios sin revisión o acción de terceros alterada introducen código inseguro | 2 | 3 | 6 | SHAs, hashes, permisos mínimos, CODEOWNERS y protección activa de main; revisión humana de cada cambio |
| A11 | Telemetría F4 | I/T | TLS desactivado y destino externo permiten fuga o alteración | 2 | 3 | 6 | Parche rechazado; Semgrep detecta verify=False; sin telemetría en versión final |
| A12 | Disponibilidad | D | Despliegue sin rollback interrumpe la lectura en turno crítico | 2 | 3 | 6 | Paquete trazable; validación de fabricante, ventana y rollback pendientes |

## Relación entre flujos y amenazas

| Flujo del DFD | Amenaza vinculada | Control y alcance |
|---|---|---|
| F1 · Operador → HMI | A01: suplantación de identidad; A05: operación sin atribución | Identidad, rol y auditoría propuestos; la interfaz HMI no está implementada. |
| F2 · HMI → lector | A02: registro manipulado o entrada tipo comando | Validación de entero y rango implementada y probada; sin shell. |
| F3 · Lector → PLC | A01: uso indebido de credencial; A03: acceso desde red abierta | Variable de entorno y análisis de política implementados; PLC y segmentación física solo modelados. |
| F4 · PLC → lector → HMI | A04: lectura alterada; A11: fuga o alteración de telemetría | Validador y rechazo del parche implementados; integridad del sensor real pendiente. |
| F5 · IA → lector | A07: extracción por prompt injection; A08: escalamiento a escritura | Diseño de consulta sin secretos y práctica externa documentada; no existe agente con herramientas en el programa. |

## Activos y debilidades

Los activos principales son la continuidad del tratamiento, la integridad de lecturas, las credenciales del controlador, el acceso del operador, el código con su historial y el paquete desplegable. Las amenazas relevantes incluyen suplantación, manipulación, interrupción del servicio, fuga de secretos y compromiso de dependencias. Las debilidades que analizamos son secretos en configuración, ejecución de shell, TLS desactivado, red abierta, versiones no fijadas y permisos excesivos del asistente.

El riesgo físico se expresa como posibilidad en el modelo. Ninguna de las pruebas alteró agua, equipos o pacientes reales. Los escáneres detectan patrones de software y configuración; por sí solos no verifican la seguridad del proceso industrial.
