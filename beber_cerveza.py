"""
Programa que indica si un joven puede beber cerveza
Debe tener 18 o más años o debe tener 16 o más años 
y estar acompañado de un adulto
"""

edad = int( input ("Edad del Joven") )
adulto = input ("Esta acompa#ado de un adulto (si/no) ")

mayor_valido = (edad >= 18)
menor_conadulto_valido = (edad >= 16 and adulto == "si")

valido = mayor_valido or menor_conadulto_valido
print valido
