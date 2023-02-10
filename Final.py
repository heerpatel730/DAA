
import time as t
import matplotlib.pyplot as plt
import numpy as np


def Insertionsort(array):
  size = len(array)
  for sorted_index in range(1, size):
        i = array[sorted_index]
        j = sorted_index
        while j > 0 and array[j - 1] > i:
            array[j] = array[j -1]
            j = j - 1
        array[j] = i
        
def Mergesort(array):
  size = len(array)
  if size > 1:
    mid = len(array)//2
    first_half = array[:mid]
    second_half = array[mid:]
    Mergesort(first_half)
    Mergesort(second_half)
    i = j = 0
    sorted_index = 0

    while (i < len(first_half)) and (j < len(second_half)) :
      if (first_half[i] < second_half[j]) :
        array[sorted_index] = first_half[i]
        i+=1
      else:
        array[sorted_index] = second_half[j]
        j+=1
      sorted_index += 1
    
    while (i < len(first_half)):
      array[sorted_index] = first_half[i]
      i+=1
      sorted_index += 1
    
    while (j < len(second_half)):
      array[sorted_index] = second_half[j]
      j+=1
      sorted_index += 1

def radix_sort(arr):
    RADIX = 10
    placement = 1
    max_digit = max(arr)

    while placement < max_digit:
      buckets = [list() for _ in range( RADIX )]
      for i in arr:
        tmp = int((i / placement) % RADIX)
        buckets[tmp].append(i)
      a = 0
      for b in range( RADIX ):
        buck = buckets[b]
        for i in buck:
          arr[a] = i
          a += 1
      placement *= RADIX

def heapify(arr, n, i):
       largest = i  
       l = 2 * i + 1     
       r = 2 * i + 2
       if ((l < n) and (arr[i] < arr[l])):
           largest = l
   
       if r < n and arr[largest] < arr[r]:
            largest = r

       if largest != i:
           arr[i],arr[largest] = arr[largest],arr[i]  

           heapify(arr, n, largest)

def heapSort(arr):
        n = len(arr)
        for i in range(n // 2 - 1, -1, -1):
            heapify(arr, n, i)
      
        
        for i in range(n-1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]   
            heapify(arr, i, 0)    
def partition(start,end, arr):

    pivot_index=start
    pivot=arr[pivot_index]

    while (start < end):

         while start < len(arr) and arr[start] <= pivot :

             start+=1

             while arr[end] > pivot:
                 end-=1

         if (start<end):
             arr[start],arr[end]=arr[end],arr[start]
             arr[end],arr[pivot_index]=arr[pivot_index],arr[end]

    return end

def quick(start,end,arr):

    if(start<end):

        p= partition(start,end,arr)


        quick(start,p-1,arr)
        quick(p+1,end,arr)  

        
def Sorter():
  M_times = []
  R_times = []
  I_times = []
  H_times = []
  Q_times = []
  
  for i in range(1, 1000):
    test_array = np.random.randint(-999999, 999999,i)
    test_array1 = test_array
    start_M = t.time()
    Mergesort(test_array)
    end_M = t.time() - start_M
    M_times.append(end_M)
    
    start_R = t.time()
    radix_sort(test_array1)
    end_R = t.time() - start_R
    R_times.append(end_R)
    
    start_I = t.time()
    Insertionsort(test_array1)
    end_I = t.time() - start_I
    I_times.append(end_I)
    
    start_H = t.time()
    heapSort(test_array1)
    end_H = t.time() - start_H
    H_times.append(end_H)
    
    start_Q = t.time()
    quick(0,len(test_array1)-1,test_array1)
    end_Q = t.time() - start_Q
    Q_times.append(end_Q)
    
  plot1, = plt.plot( H_times, list(range(1, 1000)))
  plot2, = plt.plot( R_times, list(range(1, 1000)))
  plot3, = plt.plot( I_times, list(range(1, 1000)))
  plot4, = plt.plot( M_times, list(range(1, 1000)))
  plot5, = plt.plot( Q_times, list(range(1, 1000)))
  plt.legend([plot1, plot2, plot3, plot4],["Heap sort","Radix sort", "Insertion","Merge sort","Quick Sort"])
  plt.xlabel("time")
  plt.ylabel("size")
  plt.title("Sort times")
  plt.show()

Sorter()