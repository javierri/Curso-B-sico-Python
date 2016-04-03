
# Mayor de tres números

num1 = int( input ("Numero 1") )
num2 = int( input ("Numero 2") )
num3 = int( input ("Numero 3") )

if (num1 > num2 and num1 > num3):
    print "el mayor es el primero", num1
else:
    if (num2 > num3):
        print "el mayor es el segundo", num2
    else:
        print "el mayor es el tercero", num3
