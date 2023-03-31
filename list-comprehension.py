
### List-comprehension/compresion de lista ### 3 maneras de hacer lo mismo
## Imprimir 3 listas iguales ###

my_original_list = [0,1,2,3,4,5,6,7] #lista con un rango de 0 aa 7
print(my_original_list)


my_range = range(8) # crea un rango de numeros de 0 a 7
print(list(my_range)) #crea e imprime una lista con un rango de 0 a 7


my_list = [i for i in my_range] #el for in genera un metodo de acotar una lista
print(my_list)
