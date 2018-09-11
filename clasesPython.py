#clasesPython.py


class Miclase(object):
	def __init__(self, name):
		self.name = name

	def get_name(self):
		return self.name

	def set_name(self, name):
		self.name = name
		return self.name



#Miclase objeto = new Miclase("John wick");

objeto = Miclase("John Wick")

print(objeto.get_name())
print(objeto.set_name("Neo"))