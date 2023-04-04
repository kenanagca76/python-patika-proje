"""
2- Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün. Örnek olarak:

input: [[1, 2], [3, 4], [5, 6, 7]]

output: [[[7, 6, 5], [4, 3], [2, 1]]
"""

def reverse_list(k):
 k = k[::-1]
 k = [i[::-1] for i in k]
 return k

input=[[1, 2], [3, 4], [5, 6, 7]]


print(reverse_list(input))

