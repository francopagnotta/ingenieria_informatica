# 11. En un almacén están buscando la forma de hacer los cobros más automáticamente. Para esto, se nos
# pide crear una función que reciba un número entero que representa lo que hay que cobrar, le pida al
# usuario ingresar un monto, y se vaya mostrando por pantalla cuánto falta para completar el pago.

# Repetir este proceso hasta que la deuda sea 0 o menor. Por ejemplo, si se recibe el monto 30:
	# > El importe a pagar es de 30 pesos. Por favor, ingrese un monto.
	# > 10
	# > El importe a pagar es de 20 pesos. Por favor, ingrese un monto.
	# > 15
	# > El importe a pagar es de 5 pesos. Por favor, ingrese un monto.
	# > 5


def getPayment(amount_to_receive):
	user_amount = 0

	while user_amount < amount_to_receive:
		difference = amount_to_receive - user_amount
		user_amount += int(input(f"The price to pay is ${difference}, please enter the money: $"))
	else:
		if user_amount > amount_to_receive:
			difference = abs(amount_to_receive - user_amount)
			print(f"Your change is: ${difference}")
   
	print("Thank you for buy in our store! Good Bye")

getPayment(1500)


