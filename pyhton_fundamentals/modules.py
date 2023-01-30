##import functions_annotations as calc

from my_modules.functions_annotations import sum_of as suma, product_of as multiplicar
from classes import Vehicle

mi_vehicle = Vehicle("Chevrolet", 3, 4)
print(mi_vehicle)



# result = calc.sum_and_product_of(3, 4)
resultado = suma(4,4)
producto = multiplicar(4,4)
print(f"La suma es {resultado} y el producto es {producto}")
