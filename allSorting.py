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

#Merge

def merge_sort(array):
  if(len(array) == 1):
    return

  middle_index = len(array) // 2

  left_partition = array[:middle_index]

  right_partition = array[middle_index:]

  merge_sort(left_partition)
  merge_sort(right_partition)

  i = j = k = 0

  while i < len(left_partition) and j < len(right_partition):
    if left_partition[i] < right_partition[j]:
      array[k] = left_partition[i]
      i += 1
    else:
      array[k] = right_partition[j]
      j += 1
    k += 1

  while i < len(left_partition):
    array[k] = left_partition[i]
    i += 1
    k += 1

  while j < len(right_partition):
    array[k] = right_partition[j]
    j += 1
    k += 1

#Bubble

def bubble_sort(array):
  for i in range(len(array) - 1):
    for j in range(len(array) - i - 1):
      if(array[j] > array[j+1]):
        array[j], array[j+1] = array[j+1], array[j]

#Creating the array

def create_unsorted_list(n):
    power = 10**n
    return rn.choices(range(0,power), k=power)


# sizes = []
sizes_bubble = []
# timesQuickSort = []
# timesMergeSort = []
timesBubbleSort = []

# #Run quicksort
# for i in range(1,9):
#     array = create_unsorted_list(i)
#     setup = f"from __main__ import quicksort, array; import random as rn"
#     time_taken = timeit.timeit("quicksort(array)", setup=setup, number=1)
#     sizes.append(10**i)
#     timesQuickSort.append(time_taken)
#     print("Quicksort se demora:")
#     print("--- %s segundos ---" % time_taken)
#     print("para ordenar un arreglo de tamaño 10 ^", i)
#     print("-------------------------------------------------")

# print("Fin de la prueba")

# #Run mergesort
# for i in range(1,9):
#     array = create_unsorted_list(i)
#     setup = f"from __main__ import merge_sort, array; import random as rn"
#     time_taken = timeit.timeit("merge_sort(array)", setup=setup, number=1)
#     timesMergeSort.append(time_taken)
#     print("Merge sort se demora:")
#     print("--- %s segundos ---" % time_taken)
#     print("para ordenar un arreglo de tamaño 10 ^", i)
#     print("-------------------------------------------------")

# print("Fin de la prueba")

#Run Bubblesort
for i in range(1,6):
    array = create_unsorted_list(i)
    setup = f"from __main__ import bubble_sort, array; import random as rn"
    time_taken = timeit.timeit("bubble_sort(array)", setup=setup, number=1)
    sizes_bubble.append(10**i)
    timesBubbleSort.append(time_taken)
    print("Bubble sort se demora:")
    print("--- %s segundos ---" % time_taken)
    print("para ordenar un arreglo de tamaño 10 ^", i)
    print("-------------------------------------------------")

print("Fin de la prueba")


#PLot all
# plt.plot(sizes, timesQuickSort, marker='o', label='Quicksort')
# plt.plot(sizes, timesMergeSort, marker='s', label='MergeSort')
plt.plot(sizes_bubble, timesBubbleSort, marker='^', label='BubbleSort')

plt.xlabel('Tamaño del arreglo')
plt.ylabel('Tiempo (segundos)')
plt.title('Tiempos de ejecución comparados')
plt.legend()
plt.show()

