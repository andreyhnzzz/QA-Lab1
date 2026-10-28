import unittest
from src.lab import estado_inicial, leer_expediente


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


if __name__ == "__main__":
    unittest.main()
