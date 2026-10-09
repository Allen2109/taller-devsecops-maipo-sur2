# Revisión de la propuesta de IA

**Decisión técnica:** rechazar la propuesta en su estado actual. **Fecha:** 09-10-2026.  
**Auditoría académica:** Marcela Manzor, responsable propuesto. La revisión documentada no se presenta como una firma o aprobación personal efectuada por ella.

El fragmento de la actividad importa `plc_helper_utils`, concatena registro y host dentro de un comando `modpoll`, usa `shell=True` y envía `salida.stdout` a `TELEMETRIA` mediante `requests.post(..., verify=False)`. Se conserva como propuesta en una rama independiente y no se instala ni ejecuta.

| Pregunta obligatoria | Evidencia | Respuesta y decisión |
|---|---|---|
| ¿Existe el paquete? | Consulta al registro oficial PyPI: `/pypi/plc_helper_utils/json`, respuesta HTTP 404 registrada. | No se obtuvo una distribución verificable en PyPI en esta consulta. Eso no prueba que no exista en otro registro privado. No instalar sin origen, versión, hash y aprobación. |
| ¿Qué hace con la entrada? | Concatenación de `registro` y `host` en `cmd`; `subprocess.run(cmd, shell=True, capture_output=True)`. | El shell interpreta texto externo como comandos. Un separador o sustitución podría ejecutar otra acción con permisos del lector. Semgrep detecta ese patrón. |
| ¿Apaga una protección? | `verify=False` en la llamada HTTPS. | Desactiva la validación del certificado. No asegura la identidad del servidor y facilita interceptación. Semgrep detecta el patrón. |
| ¿A dónde manda los datos? | `requests.post(TELEMETRIA, ..., data=salida.stdout)`. En el fragmento del PPT no se define el valor de TELEMETRIA. | No podemos afirmar el destino real. En la reproducción se usa `https://telemetria.invalid/ingesta`, dominio de prueba sin servicio. El envío de lecturas no está solicitado ni autorizado. |

La dependencia rechazada no figura en `requirements.txt` ni en el lock productivo. El parche no cumple los criterios de revisión aunque pudiera funcionar. No se autoriza su integración.

## Alternativa aplicada

El lector final usa `yaml.safe_load`, exige un registro entero acotado y devuelve una lectura preparada. No ejecuta `modpoll`, no usa shell, no manda telemetría y no necesita el paquete sugerido. Si después se agrega un controlador real, habrá que elegir una biblioteca oficial o validada, autenticar el destino y realizar pruebas en banco industrial aislado.

## Explicación para la persona operadora

“Este cambio podría permitir que una entrada manipulada ejecute órdenes con los permisos del lector y afectar la supervisión del tratamiento del agua. Además, enviaría las lecturas a un destino sin justificar y sin comprobar correctamente su certificado, por lo que rechazamos la propuesta hasta corregir esos riesgos.”

Este texto se elaboró con apoyo de IA y se ajustó para expresar una consecuencia posible, sin afirmar que ocurrió un incidente ni inventar el valor de TELEMETRIA. La validación y firma de los integrantes sigue siendo una responsabilidad del grupo.
