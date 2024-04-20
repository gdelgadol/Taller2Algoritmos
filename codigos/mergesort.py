import random as rn
import timeit

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

def create_unsorted_list(n):
    power = 10**n
    return rn.choices(range(0,power), k=power)

for i in range(1,10):
    array = create_unsorted_list(i)
    setup = f"from __main__ import merge_sort, array; import random as rn; array = rn.sample(array, len(array))"
    time_taken = timeit.timeit("merge_sort(array)", setup=setup, number=1)
    print("Merge sort se demora:")
    print("--- %s segundos ---" % time_taken)
    print("para ordenar un arreglo de tamaño 10 ^", i)
    print("-------------------------------------------------")

print("Fin de la prueba")