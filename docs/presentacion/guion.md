# Exposición de 90 segundos

**Relatora propuesta:** Marcela Manzor. Para cumplir el criterio presencial, debe exponer quien no haya operado el teclado durante la actividad. Este guion no acredita que la exposición ya ocurrió.

## Primeros 30 segundos: sistema e impacto

Nuestro caso es la planta de agua Maipo Sur. El software permite consultar una lectura de cloro, pero un cambio incorrecto podría dejar al operador sin información o mostrarle un valor alterado. En una planta real, eso podría afectar el tratamiento del agua. Por eso priorizamos la credencial expuesta, las entradas que ejecutan comandos y el acceso abierto al panel. Todo lo que probamos aquí es simulado.

## Siguientes 30 segundos: control y decisión

Automatizamos la búsqueda de secretos, la revisión del código, el análisis de dependencias y la configuración de red. Conservamos un ejemplo con la credencial expuesta para demostrar el fallo y una versión corregida que usa una variable de entorno. También generamos defectos temporales: las herramientas deben detectarlos para que el control se considere válido. Los resultados y la lista de materiales quedan asociados al commit en Actions.

## Últimos 30 segundos: criterio frente a la IA

Rechazamos el parche de IA porque introduce un paquete sin origen verificado, interpreta entradas mediante shell, desactiva la validación TLS y envía lecturas a un destino no justificado. Mantuvimos el lector local sin esos comportamientos. Antes de usarlo en una planta real todavía faltan pruebas industriales, segmentación efectiva, gestión de identidades y un procedimiento de recuperación aprobado por operación.

## Respuestas breves si preguntan

- ¿Por qué no borrar solo la contraseña? Porque el historial conserva el valor y hay que rotar una credencial real expuesta.
- ¿Un pipeline verde asegura la planta? Verifica estos controles de software; la seguridad física requiere pruebas y validación adicionales.
- ¿Por qué usar IA si rechazaron el parche? Ayuda a explicar y revisar, pero sus propuestas necesitan evidencia y autorización humana.
