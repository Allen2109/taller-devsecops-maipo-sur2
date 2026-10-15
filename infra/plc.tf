# Modelo documental inerte: sin providers, recursos, credenciales ni estado remoto.
# Describe el caso de laboratorio; no crea infraestructura.
variable "origen_panel_simulado" {
  type        = string
  default     = "192.0.2.0/24"
  description = "Red documental para la política de acceso del panel ficticio"
}
locals {
  panel_simulado = {
    protocolo = "tcp"
    puerto    = 443
    origen    = var.origen_panel_simulado
    modo      = "simulacion"
  }
}
