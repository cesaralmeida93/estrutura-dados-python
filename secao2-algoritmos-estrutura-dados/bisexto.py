def bisexto(ano):
	if (ano % 100) != 0 and (ano % 4) == 0 or (ano % 400) == 0:
		print("Bisexto")
	else:
		print("Não é Bisexto") 