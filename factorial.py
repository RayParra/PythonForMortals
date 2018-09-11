#factorial.py


def factorial(n=1, fact=1):
	for i in range(1, n):
		fact *= (i+1)

	return fact


n = int(input("Escribe un numero para calcular el factorial: --- "))

print(factorial(n))