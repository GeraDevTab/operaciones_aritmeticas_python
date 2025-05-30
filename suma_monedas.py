#Ejercicio 2. Definir la funcion
#   sumaMonedas: (int, int, int, int, int) -> int
#tal que sumaMonedas (a,b,c,d,e) es la suma de los euros
#correspondientes a a monedas de 1 euro, b de 2 euro, b de 2 euros,
#c de 5 euros, d de 10 euros y e de 20 euros. Por ejemplo,
#   sumaMonedas(0,0,0,0,1) == 20
#   sumaMonedas(0,0,8,0,3) == 100
#   sumaMonedas(1,1,1,1,1) == 38
#----------

def sumaMonedas(a:int, b:int, c:int, d:int, e:int) -> int:
    return 1*a + 2*b + 5*c + 10*d + 20*e

print(sumaMonedas(0,0,0,0,1))