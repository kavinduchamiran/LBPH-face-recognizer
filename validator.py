from scipy import misc
from scipy.misc import toimage
import numpy as np
import collections
import csv
 
histogram = dict.fromkeys(range(8*8*256), 0)
histogram2 = {}

def blockshaped(arr):
    blocks = []
    x = np.array(arr)
    for i in range(0,256,32):
        for j in range(0,256,32):
            blocks.append(x[i:i+32, j:j+32])
    return blocks
        

arr = misc.imread('training/test.jpg', True)

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

blocks = blockshaped(arr)

for block in range(64):
    for i in blocks[block]:
        for j in i:
            histogram[(block+1)*(j+1)] = 1
    
with open('output.csv') as pscfile:
    reader = csv.reader(pscfile)
    next(reader)
    results = dict(reader)

results = {float(k):int(v) for k,v in results.items()}

final = 0

for key in results.keys():
    old = histogram[key]
    new = results[key]
    diff = old - new
    final += diff**2

print final**.5
