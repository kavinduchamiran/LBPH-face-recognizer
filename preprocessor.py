from scipy import misc
from scipy.misc import toimage
import numpy as np
import collections
import csv
 
histogram = dict.fromkeys(range(8*8*256), 0)

def blockshaped(arr):
    blocks = []
    x = np.array(arr)
    for i in range(0,256,32):
        for j in range(0,256,32):
            blocks.append(x[i:i+32, j:j+32])
    return blocks
        
            

for i in range(1):
    arr = misc.imread('training/face1.jpg', True)
    
    for i in range(1,len(arr)-1):
        for j in range(1,len(arr[i])-1):
            a = []
            cell = arr[i][j]

            a.append(arr[i-1][j-1])
            a.append(arr[i-1][j])
            a.append(arr[i-1][j+1])
            a.append(arr[i][j-1])
            a.append(arr[i][j+1])
            a.append(arr[i+1][j-1])
            a.append(arr[i+1][j])
            a.append(arr[i+1][j+1])
            
            for item in range(len(a)):
                a[item] = ('1' if (a[item] >= cell) else '0')

            k = int(''.join(a), 2)
            arr[i][j] = k

block_id = 0

blocks = blockshaped(arr)

for block in range(64):
    for i in blocks[block]:
        for j in i:
            histogram[(block+1)*(j+1)] = 1
            
w = csv.writer(open("output.csv", "w"))
for key, val in histogram.items():
    w.writerow([key, val])


#add loop

