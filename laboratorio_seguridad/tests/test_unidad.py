import unittest
from src.lab import estado_inicial, leer_expediente, actualizar_nota, revocar_sesion


class LecturaExpedientes(unittest.TestCase):
    def setUp(self):
        self.estado = estado_inicial()

    def test_tc01_estudiante_lee_expediente_propio(self):
        codigo, datos = leer_expediente(self.estado, "lab-ana", "101")
        self.assertEqual(200, codigo)
        self.assertEqual("ana", datos.get("estudiante"))
        self.assertEqual(82, datos.get("nota"))

    def test_tc03_admin_lee_expedientes_de_ambas_sedes(self):
        for expediente_id in ("101", "202"):
            with self.subTest(expediente=expediente_id):
                codigo, datos = leer_expediente(self.estado, "lab-admin", expediente_id)
                self.assertEqual(200, codigo)
                self.assertEqual(expediente_id, datos.get("id"))

    def test_tc04a_estudiante_no_lee_expediente_ajeno(self):
        codigo, datos = leer_expediente(self.estado, "lab-ana", "202")
        self.assertEqual(403, codigo, "un estudiante leyo el expediente de otra persona")
        self.assertNotIn("nota", datos, "la denegacion filtro la nota")
        self.assertNotIn("estudiante", datos)
        self.assertEqual(91, self.estado["expedientes"]["202"]["nota"])

    def test_tc04b_docente_no_lee_expediente_de_otra_sede(self):
        codigo, datos = leer_expediente(self.estado, "lab-maria", "202")
        self.assertEqual(403, codigo, "un docente leyo un expediente de otra sede")
        self.assertNotIn("nota", datos, "la denegacion filtro la nota")

    def test_docente_lee_expediente_de_su_sede(self):
        codigo, datos = leer_expediente(self.estado, "lab-pedro", "202")
        self.assertEqual(200, codigo)
        self.assertEqual(91, datos.get("nota"))


class Sesiones(unittest.TestCase):
    def setUp(self):
        self.estado = estado_inicial()

    def test_tc06_sesion_revocada_no_lee_ni_modifica(self):
        codigo, _ = revocar_sesion(self.estado, "lab-maria")
        self.assertEqual(200, codigo)
        codigo, datos = leer_expediente(self.estado, "lab-maria", "101")
        self.assertEqual(401, codigo, "una sesion revocada pudo leer")
        self.assertNotIn("nota", datos)
        codigo, _ = actualizar_nota(self.estado, "lab-maria", "101", 10)
        self.assertEqual(401, codigo, "una sesion revocada pudo modificar")
        self.assertEqual(82, self.estado["expedientes"]["101"]["nota"])

    def test_tc07_sesion_vencida_no_lee_ni_modifica(self):
        codigo, datos = leer_expediente(self.estado, "lab-vencida", "101")
        self.assertEqual(401, codigo, "una sesion vencida pudo leer")
        self.assertNotIn("nota", datos)
        codigo, _ = actualizar_nota(self.estado, "lab-vencida", "101", 10)
        self.assertEqual(401, codigo, "una sesion vencida pudo modificar")
        self.assertEqual(82, self.estado["expedientes"]["101"]["nota"])

    def test_token_desconocido_o_vacio_es_rechazado(self):
        for token in ("lab-inexistente", ""):
            with self.subTest(token=token):
                codigo, datos = leer_expediente(self.estado, token, "101")
                self.assertEqual(401, codigo)
                self.assertNotIn("nota", datos)


class ModificacionNotas(unittest.TestCase):
    def setUp(self):
        self.estado = estado_inicial()

    def test_tc02_docente_actualiza_nota_en_su_sede(self):
        codigo, datos = actualizar_nota(self.estado, "lab-maria", "101", 85)
        self.assertEqual(200, codigo)
        self.assertEqual(85, datos.get("nota"))
        self.assertEqual(85, self.estado["expedientes"]["101"]["nota"])

    def test_tc05_docente_no_modifica_nota_de_otra_sede(self):
        codigo, datos = actualizar_nota(self.estado, "lab-maria", "202", 10)
        self.assertEqual(403, codigo, "un docente modifico una nota de otra sede")
        self.assertNotIn("nota", datos)
        self.assertEqual(91, self.estado["expedientes"]["202"]["nota"])

    def test_tc08_estudiante_y_admin_no_modifican_notas(self):
        for token in ("lab-ana", "lab-admin"):
            with self.subTest(token=token):
                codigo, datos = actualizar_nota(self.estado, token, "101", 100)
                self.assertEqual(403, codigo)
                self.assertNotIn("nota", datos)
                self.assertEqual(82, self.estado["expedientes"]["101"]["nota"])


if __name__ == "__main__":
    unittest.main()
