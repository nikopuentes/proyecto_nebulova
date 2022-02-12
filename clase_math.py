# por norma general importar librerias al inicio de cada codigo
import math
from math import ceil
import statistics
# import math as mt
# from math import sin as se

dir(math)
help(math)
# https://docs.python.org/3.8/library/math.html


math.ceil(5.9) # redondear al numero entero superior
ceil(3.1) # solo cuando importo la funcion directamente
math.floor(5.9) # redondear al numero entero inferior

math.pi
math.inf
math.nan # float('nan')
math.nan + 6 # cualquier operacion con un número nan es nan

math.fabs(-5)
abs(-5)

math.pow(2, 3) # math.pow(x, y) ---> elevar un numero x por y

math.log(5)
math.log1p(5) # math.log(x +1)

5 ** (1/2)
math.sqrt(5)

math.isnan(math.nan) # True o False si el valor es nan o no
math.isnan(5)
math.isinf(math.inf) # True o False si el valor es infinito o no
math.isinf(6)

a = [1,2,3]
b = [2,3,4]
math.dist(a, b)


valores = [11,2,3,1,7,9,20,1, 11,3,4,3]
statistics.mean(valores)
statistics.median(valores)
statistics.mode(valores)
statistics.quantiles(valores, n=4, method='exclusive')
statistics.quantiles(valores, method='inclusive')



# Ejercicio 6 

P = (0.5, 0.1, 0.6) 

sumatorio = 0 

for i in P: 
    sumatorio += i**2 

distancia = sumatorio ** (1/2) 

 

if distancia > 1: 
    print("fuera") 

else: 
    print("dentro") 










