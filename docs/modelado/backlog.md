# Backlog de seguridad

Cada amenaza tiene una historia y un criterio observable. La prioridad se define por el impacto físico del modelo. Los responsables son una propuesta de distribución académica, no firmas de aprobación realizadas.

| Historia | Amenaza | Requisito y criterio de aceptación | Responsable | Estado |
|---|---|---|---|---|
| SS01 | A01 | Como operador, necesito que el secreto no esté en código. Gitleaks falla con el ejemplo; lector falla sin variable y no imprime su contenido. | Miguel | Implementado |
| SS02 | A02 | Como mantenedor, necesito rechazar entradas tipo comando. Registros no enteros o fuera de 1-100 fallan; no se invoca shell. | Miguel | Implementado |
| SS03 | A03 | Como operador, necesito que el panel no acepte cualquier origen. Trivy detecta 0.0.0.0/0 de prueba; modelo final restringido. | Franco | Control estático implementado |
| SS04 | A04 | Como operador, necesito rechazar valores inválidos. NaN, infinito y datos fuera del rango didáctico fallan. | Miguel | Implementado y probado |
| SS05 | A05 | Como auditor, necesito atribuir órdenes a una identidad. Toda modificación debe registrar identidad y tiempo en almacenamiento protegido. | Marcela | Propuesto; 16-10-2026 |
| SS06 | A06 | Como guardián, necesito inventario verificable. Dependencia fijada y con hash, escaneos y SBOM generada. | Franco | Implementado |
| SS07 | A07 | Como operador, necesito que la IA no reciba credenciales. Pruebas de inyección no deben revelar datos ni habilitar herramientas. | Marcela | Diseño y práctica Agent Breaker documentada; sin agente conectado al lector |
| SS08 | A08 | Como operador, necesito impedir escrituras de IA. Cuenta del asistente solo lectura y aprobación humana externa para cambios. | Marcela | Propuesto; sin agente desplegado |
| SS09 | A09 | Como turno, necesito lectura disponible. Carga y rate limiting deben demostrar límites y alertas antes del despliegue. | Franco | Pendiente; 16-10-2026 |
| SS10 | A10 | Como revisor, necesito bloquear merges inseguros. PR, revisión y status checks obligatorios sobre main. | Franco | Ver estado efectivo en evidencias |
| SS11 | A11 | Como operador, necesito destinos autorizados y TLS activo. Rechazar verify=False y envío no justificado. | Marcela | Parche rechazado; SAST implementado |
| SS12 | A12 | Como operador, necesito recuperar el servicio ante un despliegue fallido. Probar rollback en banco aislado y autorizar ventana. | Franco | Pendiente antes de planta real |

## Casos de abuso

Un tercero obtiene una credencial del repositorio y bloquea al turno. Un usuario introduce texto de comandos donde debería indicar un registro. Una propuesta de IA agrega una dependencia no aprobada y remite lecturas a un servidor no solicitado. Para cada caso se exige evidencia de detección y una decisión antes de integrar el cambio.
