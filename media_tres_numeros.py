#Ejercicio 1. Definir la funcion
#   media3 : (float, float, float) -> float
# tal que (media3 x y z) es la media aritmetica de los numeros x, y y z. Por ejemplo
# media3(1,3,8) == 4.0
# media3(-1,0,7) == 2.0
# media3(-3,0,3) == 0.0

def media3(x:float, y:float, z: float) -> float:
    return (x + y + z)/3

print(media3(1,3,8))
print(media3(-1,0,7))
print(media3(-3,0,3))