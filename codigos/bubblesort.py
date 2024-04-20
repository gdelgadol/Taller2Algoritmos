import random as rn
import timeit

def bubble_sort(array):
  for i in range(len(array) - 1):
    for j in range(len(array) - i - 1):
      if(array[j] > array[j+1]):
        array[j], array[j+1] = array[j+1], array[j]

def create_unsorted_list(n):
    power = 10**n
    return rn.choices(range(0,power), k=power)

for i in range(1,6):
    array = create_unsorted_list(i)
    setup = f"from __main__ import bubble_sort, array; import random as rn; array = rn.sample(array, len(array))"
    time_taken = timeit.timeit("bubble_sort(array)", setup=setup, number=1)
    print("Bubble sort se demora:")
    print("--- %s segundos ---" % time_taken)
    print("para ordenar un arreglo de tamaño 10 ^", i)
    print("-------------------------------------------------")

print("Fin de la prueba")