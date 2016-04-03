
# Programa que determina si un platano es grande (15 cm o más)
# y es amarillo 

tam = int( input ("El tama#o del platano") )
color = input ("Color del platano ")

tam_valido = (tam >= 15)
color_valido = (color == "Amarillo" or color == "amarillo")

valido = tam_valido and color_valido
print valido
