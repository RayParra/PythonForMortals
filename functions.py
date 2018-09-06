#functions.py


# # by User

def hello(name="Anonimo"):
	return "Hello World!", name

def sumar(x=1, y=2):
	return x + y


x = int(input("Escribe un Numero: ---"))
y = int(input("Escribe otro Numero: ---"))


print(sumar(x, y))