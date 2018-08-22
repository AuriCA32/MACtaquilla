from django.test import TestCase
from taquillaAPI.models import *
from django.forms import ModelForm
from taquillaAPI.forms import *

class TaquillaTestCase(TestCase):
	def setUp(self):
		pass

	def cliente_crear_test(self):
		form_data = {
			'cedula': 21759474,
			'nombre': "José",
			'apellido': "Basanta",
			'telefono': "04241642685"
		}
		form = Cliente(data=form_data)
		form.save()
		cliente = Cliente.objects.get(cedula=21759474)
		self.assertEqual(cliente.Cliente, "José")