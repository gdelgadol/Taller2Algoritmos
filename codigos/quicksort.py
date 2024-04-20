import random as rn
import timeit

def quicksort(array):

    def partition(array, start, end):
        smallest = start
        pivot_index = rn.randint(start, end)
        array[pivot_index], array[end] = array[end], array[pivot_index]
        pivot = array[end]
        for i in range(start, end):
            if array[i] <= pivot:
                array[i], array[smallest] = array[smallest], array[i]
                smallest += 1
        array[smallest], array[end] = array[end], array[smallest]
        return smallest

    def recursive_quicksort(array, start, end):
        if start < end:
            pivot = partition(array, start, end)
            recursive_quicksort(array, start, pivot - 1)
            recursive_quicksort(array, pivot + 1, end)

    recursive_quicksort(array, 0, len(array) - 1)

def create_unsorted_list(n):
    power = 10**n
    return rn.choices(range(0,power), k=power)

array = create_unsorted_list(9)
setup = f"from __main__ import quicksort, array; import random as rn; array = rn.sample(array, len(array))"
time_taken = timeit.timeit("quicksort(array)", setup=setup, number=1)
print("Quicksort se demora:")
print("--- %s segundos ---" % time_taken)
print("para ordenar un arreglo de tamaño 10 ^", i)
print("-------------------------------------------------")
print("Fin de la prueba")
