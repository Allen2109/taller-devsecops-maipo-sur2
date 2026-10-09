# Modelo de configuración para análisis estático. No ejecutar terraform apply.
# Sin provider configurado, credenciales ni backend remoto.
resource "aws_security_group" "panel_simulado" {
  name        = "panel-maipo-sur-laboratorio"
  description = "Representación del acceso restringido al panel"
  ingress {
    description = "HTTPS desde red documental de laboratorio"
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["192.0.2.0/24"]
  }
  egress {
    description = "Salida limitada a la red documental"
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["192.0.2.0/24"]
  }
}
