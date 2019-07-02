from bubblesort import bubble_sort
from selectionsort import selection_sort
from insertionsort import insert_sort
from quicksort import quick_sort
import time

list01 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
start = time.time()
# bubble_sort(list01)
# selection_sort(list01)
# insert_sort(list01)
quick_sort(list01, 0, 8)
print(time.time()-start)
print(list01)