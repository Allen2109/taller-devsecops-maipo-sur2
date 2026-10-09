import contextlib
import io
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from src.lector_cloro import leer_cloro_simulado, validar_lectura


class LecturaTest(unittest.TestCase):
    def setUp(self):
        self.entorno = patch.dict(os.environ, {"PLC_PASSWORD": "valor-ficticio-unittest"})
        self.entorno.start()
        self.addCleanup(self.entorno.stop)

    def test_lectura_correcta(self):
        self.assertEqual(leer_cloro_simulado()["cloro_mg_l"], 0.7)
        self.assertTrue(leer_cloro_simulado()["simulado"])

    def test_sin_variable_falla(self):
        with patch.dict(os.environ, {}, clear=True):
            with self.assertRaises(RuntimeError):
                leer_cloro_simulado()

    def test_variable_vacia_falla(self):
        with patch.dict(os.environ, {"PLC_PASSWORD": "  "}):
            with self.assertRaises(RuntimeError):
                leer_cloro_simulado()

    def test_no_filtra_credencial(self):
        salida = io.StringIO()
        with contextlib.redirect_stdout(salida), self.assertLogs("src.lector_cloro", level="INFO") as logs:
            leer_cloro_simulado()
        self.assertNotIn(os.environ["PLC_PASSWORD"], salida.getvalue()+str(logs.output))

    def test_entrada_comando_rechazada(self):
        for valor in ["1; id", "$(id)", "1", True, 0, 101]:
            with self.subTest(valor=valor), self.assertRaises(ValueError):
                leer_cloro_simulado(registro=valor)

    def test_registros_limite(self):
        for n in [1,100]: self.assertTrue(leer_cloro_simulado(registro=n)["simulado"])

    def test_config_con_password_rechazada(self):
        with tempfile.TemporaryDirectory() as directorio:
            f=Path(directorio)/"config.yaml"
            f.write_text("modo: simulacion\npassword: valor-ficticio\npassword_env: PLC_PASSWORD\n")
            with self.assertRaises(ValueError): leer_cloro_simulado(f)

    def test_modo_real_rechazado(self):
        with tempfile.TemporaryDirectory() as directorio:
            f=Path(directorio)/"config.yaml"
            f.write_text("modo: real\n")
            with self.assertRaises(ValueError): leer_cloro_simulado(f)

    def test_lecturas_invalidas(self):
        for n in [float("nan"),float("inf"),-1,6,"0.7",True]:
            with self.subTest(n=n), self.assertRaises(ValueError): validar_lectura(n)

    def test_rango_didactico(self):
        for n in [0,0.7,5]: self.assertEqual(validar_lectura(n),n)
