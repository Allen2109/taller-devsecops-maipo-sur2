# METADATA
# title: Acceso global al panel operacional
# description: El panel del laboratorio debe limitar los orígenes aprobados.
# custom:
#   id: LAB-ICS-001
#   severity: CRITICAL
#   recommended_actions: Limitar el origen a la red operacional aprobada.
#   input:
#     selector:
#     - type: yaml
package user.industrial.LABICS001

deny[msg] {
    input.sistema == "panel-operacional-laboratorio"
    input.origenes_permitidos[_] == "0.0.0.0/0"
    msg := "El panel operacional permite acceso desde cualquier origen"
}
