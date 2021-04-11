def dollar_to_euro(dollar_value):
	return dollar_value * 0.89

def euro_to_yen(euro_value):
	return euro_value * 124.15

####### ↓ YOUR CODE BELOW ↓ #######

dollar_eu = dollar_to_euro(137)

total_amount = euro_to_yen(dollar_eu)

print (total_amount)


"""SOLUCION: Creo una variable donde ingreso los 137. Y otra para el PRODUCTO de las dos funciones (total_amount)"""