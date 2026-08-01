from django.test import TestCase

from academico.models import Carrera, Facultad, Materia


class AcademicRelationsTests(TestCase):
    def test_carrera_belongs_to_facultad_and_materia_links_to_it(self):
        facultad = Facultad.objects.create(nombre='Facultad de Ingeniería')
        carrera = Carrera.objects.create(nombre='Ingeniería de Sistemas', facultad=facultad)
        materia = Materia.objects.create(
            nombre='Programación',
            codigo='PROG-101',
            creditos=5,
            semestre=1,
            carrera=carrera,
        )

        self.assertEqual(materia.carrera.facultad, facultad)
        self.assertEqual(carrera.facultad.nombre, 'Facultad de Ingeniería')
