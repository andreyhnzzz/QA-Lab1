import http.client
import json
import threading
import unittest
from http.server import ThreadingHTTPServer

from servidor import ServidorLaboratorio
from src.lab import estado_inicial


class ManejadorSilencioso(ServidorLaboratorio):
    def log_message(self, fmt, *args):
        pass


class ApiExpedientes(unittest.TestCase):
    def setUp(self):
        ManejadorSilencioso.estado = estado_inicial()
        self.estado = ManejadorSilencioso.estado
        self.servidor = ThreadingHTTPServer(("127.0.0.1", 0), ManejadorSilencioso)
        self.servidor.daemon_threads = True
        threading.Thread(target=self.servidor.serve_forever, daemon=True).start()
        self.addCleanup(self.servidor.server_close)
        self.addCleanup(self.servidor.shutdown)

    def pedir(self, metodo, ruta, token=None, cuerpo=None, longitud=None):
        conexion = http.client.HTTPConnection("127.0.0.1", self.servidor.server_port, timeout=3)
        try:
            conexion.putrequest(metodo, ruta)
            if token:
                conexion.putheader("Authorization", "Bearer " + token)
            if cuerpo is not None or longitud is not None:
                datos = cuerpo.encode() if isinstance(cuerpo, str) else (cuerpo or b"")
                conexion.putheader("Content-Type", "application/json")
                conexion.putheader("Content-Length", str(len(datos) if longitud is None else longitud))
                conexion.endheaders(datos)
            else:
                conexion.endheaders()
            respuesta = conexion.getresponse()
            return respuesta.status, json.loads(respuesta.read().decode("utf-8"))
        finally:
            conexion.close()

    def nota(self, expediente_id):
        return self.estado["expedientes"][expediente_id]["nota"]

    def test_salud_responde_sin_credenciales(self):
        self.assertEqual((200, {"estado": "laboratorio"}), self.pedir("GET", "/health"))

    def test_tc01_api_estudiante_lee_expediente_propio(self):
        codigo, datos = self.pedir("GET", "/expedientes/101", "lab-ana")
        self.assertEqual(200, codigo)
        self.assertEqual(82, datos["nota"])

    def test_tc04_api_estudiante_no_lee_expediente_ajeno(self):
        codigo, datos = self.pedir("GET", "/expedientes/202", "lab-ana")
        self.assertEqual(403, codigo)
        self.assertEqual({"error": "Acceso denegado"}, datos)

    def test_tc05_api_docente_no_modifica_nota_de_otra_sede(self):
        codigo, datos = self.pedir("POST", "/expedientes/202/nota", "lab-maria", '{"nota": 10}')
        self.assertEqual(403, codigo)
        self.assertNotIn("nota", datos)
        self.assertEqual(91, self.nota("202"))

    def test_tc06_api_sesion_revocada_pierde_acceso(self):
        self.assertEqual(200, self.pedir("POST", "/sesiones/revocar", "lab-ana")[0])
        codigo, datos = self.pedir("GET", "/expedientes/101", "lab-ana")
        self.assertEqual(401, codigo)
        self.assertNotIn("nota", datos)

    def test_tc07_api_sesion_vencida_o_ausente_es_rechazada(self):
        for token in ("lab-vencida", None):
            with self.subTest(token=token):
                codigo, datos = self.pedir("GET", "/expedientes/101", token)
                self.assertEqual(401, codigo)
                self.assertNotIn("nota", datos)

    def test_tc09_api_entrada_invalida_devuelve_400_sin_cambios(self):
        for cuerpo in ("{no es json", "[1, 2]", '{"nota": "alta"}', '{"otro": 1}', '{"nota": NaN}'):
            with self.subTest(cuerpo=cuerpo):
                codigo, datos = self.pedir("POST", "/expedientes/101/nota", "lab-maria", cuerpo)
                self.assertEqual(400, codigo)
                self.assertNotIn("nota", datos)
                self.assertEqual(82, self.nota("101"))

    def test_tc11_api_nota_fuera_de_rango_no_se_persiste(self):
        for valor in (-1, 101):
            with self.subTest(valor=valor):
                codigo, _ = self.pedir("POST", "/expedientes/101/nota", "lab-maria", '{"nota": %d}' % valor)
                self.assertEqual(400, codigo)
                self.assertEqual(82, self.nota("101"))

    def test_tc12_api_limite_de_tamano_del_cuerpo(self):
        base = '{"nota": 70}'
        cuerpo_1024 = base + " " * (1024 - len(base))
        codigo, _ = self.pedir("POST", "/expedientes/101/nota", "lab-maria", cuerpo_1024)
        self.assertEqual(200, codigo, "el limite exacto de 1024 bytes debe aceptarse")
        codigo, datos = self.pedir("POST", "/expedientes/101/nota", "lab-maria", cuerpo_1024 + " ")
        self.assertEqual(413, codigo, "1025 bytes deben rechazarse")
        self.assertNotIn("nota", datos)
        self.assertEqual(70, self.nota("101"))

    def test_tc12b_api_content_length_negativo_se_rechaza(self):
        codigo, _ = self.pedir("POST", "/expedientes/101/nota", "lab-maria", b"", longitud=-1)
        self.assertEqual(400, codigo)
        self.assertEqual(82, self.nota("101"))

    def test_ruta_inexistente_devuelve_404(self):
        self.assertEqual(404, self.pedir("GET", "/administracion", "lab-admin")[0])


if __name__ == "__main__":
    unittest.main()
