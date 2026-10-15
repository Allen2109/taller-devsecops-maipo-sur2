# Credenciales: detección, corrección e historial

En el ejercicio inicial el defecto es una contraseña ficticia escrita directamente en `config.yaml`. La rama didáctica conserva ese escenario para que Gitleaks muestre el archivo y la regla. En main, el archivo indica `password_env: PLC_PASSWORD` y el lector obtiene el valor de `os.environ`.

La prueba funcional usa el secreto del repositorio, mientras las pruebas unitarias inyectan un dato de prueba en memoria. No hay contraseña de fábrica real ni equipo que la acepte.

## Rotación simulada del laboratorio · 14-10-2026

Ejecutamos `python scripts/simular_rotacion.py`. Primero se inicia un proceso con un valor ficticio anterior; luego otro proceso limpio con un valor sustituto distinto. Ambos conservan la misma lectura. Un tercer proceso sin la variable queda bloqueado. Se comprueba que los valores no aparezcan en las salidas y se genera `reports/rotacion-simulada.json`; el pipeline conserva ese informe junto al paquete.

La simulación demuestra sustitución de configuración y continuidad del lector. No prueba revocación en un controlador: el simulador solo exige una variable no vacía. La actualización adicional de `PLC_PASSWORD` en GitHub solicitó verificación de acceso y no quedó confirmada; el informe declara expresamente que ese secreto no fue modificado. Esta limitación no se presenta como una rotación industrial realizada.

El Gitleaks de archivos revisa el estado actual. El segundo control examina todos los commits alcanzables de main. No se omite una regla para permitir el defecto didáctico: este se conserva en otra rama y sus ejecuciones deben fallar. Al examinar todas las ramas, el valor ficticio seguirá siendo visible y detectable.

En una planta real, quitar el valor del archivo sería insuficiente. Correspondería revocarlo, cambiarlo en el controlador y en el gestor de secretos, revisar accesos desde la exposición y coordinar la limpieza del historial y sus copias. La credencial real nunca se colocaría en la ficha o captura.
