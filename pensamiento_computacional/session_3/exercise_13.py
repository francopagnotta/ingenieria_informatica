# 13. Se tiene una máquina de sacar juguetes que funciona cuando se ingresa una determinada cantidad de
# fichas, y se quiere hacer una función que imite ese comportamiento.

# a. Hacer una función que reciba un número que represente el precio de la máquina, e imprima
# por pantalla “Ingresá x fichas para comenzar” hasta que se hayan ingresado esa cantidad de
# letras F (que representan una ficha), y luego “¡A jugar!” cuando se hayan ingresado todas las
# fichas necesarias. 
# Por ejemplo, si la función recibe 3, debería tener el siguiente
# comportamiento:
	# > Ingresá 3 fichas para comenzar
	# > F
	# > Ingresá 3 fichas para comenzar
	# > F
	# > Ingresá 3 fichas para comenzar
	# > B
	# > Ingresá 3 fichas para comenzar
	# > F
	# > ¡A jugar!

# ATENCIÓN: notar cómo cuando se ingresa una letra distinta de F, esta se ignora a la hora de contar la
# cantidad de fichas que fueron ingresadas.

# b. Ahora se quiere que se vaya mostrando por pantalla, cuántas fichas FALTAN ingresar para
# empezar a jugar Es decir:
	# > Ingresá 3 fichas (F) para comenzar
	# > F
	# > Ingresá 2 fichas (F) para comenzar
	# > F
	# > Ingresá 1 fichas (F) para comenzar
	# > B
	# > Ingresá 1 fichas (F) para comenzar
	# > F
	# > ¡A jugar!

# c. Agregar a la función el mensaje de error “Por favor solamente ingrese fichas reales (F)” cuando
# se recibe una letra distinta de F.


def play():
	coins_to_play = 3
	user_input_coins = 0

	while user_input_coins < coins_to_play:
		user_input = input(f"Insert {coins_to_play - user_input_coins} (F) to play: ").lower()

		if user_input == 'f':
			user_input_coins += 1
		else:
			print("Please enter only real coins (F)")
	else: 
		print("Let's play!")

play()
		

