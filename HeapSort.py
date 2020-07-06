

inputarray=[8,89,265,78,56,245,100]
size= len(inputarray)

def maxHeap(array,n,i):
    largest = i
    leftchild= 2*i +1
    rightchild=2*i +2
    if ( leftchild<n and array[leftchild]> array[largest] ):
        largest=leftchild
    if ( rightchild<n and array[rightchild]> array[largest] ):
        largest=rightchild
    if ( largest != i):
        array[largest],array[i] = array[i],array[largest]
        maxHeap(array,n,largest)



def heapSort(array,n):
    for i in range(n//2-1,-1,-1):
        maxHeap(array,n,i)


    for i in range(n-1,0,-1):
        array[0],array[i] = array[i],array[0]
        maxHeap(array,i,0)






heapSort(inputarray,size)
print("the sorted array is ")
for i in range(size):
    print(inputarray[i])


