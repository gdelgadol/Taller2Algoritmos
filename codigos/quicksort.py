import random as rn
import timeit
import matplotlib.pyplot as plt

def quicksort(array):

  def partition(array, start, end):
    smallest = start
    #print("This is the initial smallest index:",smallest, "=",array[smallest])
    pivot_index = rn.randint(start, end)
    array[pivot_index], array[end] = array[end], array[pivot_index]
    pivot = array[end]
    #print("This is the pivot:",pivot)
    for i in range(start, end):
      #print(i)
      if (array[i] <= pivot):
        #print("Array before swap:", array)
        array[i], array[smallest] = array[smallest], array[i]
        #print("Array after swap:", array)
        smallest += 1
      #print("This is the current smallest index:",smallest, "=",array[smallest])
      #print("------------------------------------------------")

    array[smallest], array[end] = array[end], array[smallest]
    return smallest

  def recursive_quicksort(array, start, end):
    if(start < end):
      pivot = partition(array, start, end)
      recursive_quicksort(array, start, pivot - 1)
      recursive_quicksort(array, pivot + 1, end)

  recursive_quicksort(array, 0, len(array)-1)

def create_unsorted_list(n):
    power = 10**n
    return rn.choices(range(0,power), k=power)

sizes = []
times = []

for i in range(1,9):
    array = create_unsorted_list(i)
    setup = f"from __main__ import quicksort, array; import random as rn"
    time_taken = timeit.timeit("quicksort(array)", setup=setup, number=1)
    sizes.append(10**i)
    times.append(time_taken)
    print("Quicksort se demora:")
    print("--- %s segundos ---" % time_taken)
    print("para ordenar un arreglo de tamaño 10 ^", i)
    print("-------------------------------------------------")

print("Fin de la prueba")

#Plotting results
plt.plot(sizes, times, marker='o')
plt.title('Tiempo de ejecución de QuickSort')
plt.xlabel('Número de elementos a ordenar')
plt.ylabel('Tiempo (segundos)')
plt.grid(True)
plt.show()