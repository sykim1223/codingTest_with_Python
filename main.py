from random import randint
import time

array = []
for _ in range(10000):
  array.append(randint(1, 100))

#selection sort performance 
start_time = time.time()

#selection sort
for i in range(len(array)):
  min_index = i #minimum elem min_index
  for j in range(i+1, len(array)):
    if array[min_index] > array[j]:
      min_index = j
  array[i], array[min_index] = array[min_index], array[i] #swap
  
end_time = time.time()
print("1. Selection sort perform: ", end_time - start_time)