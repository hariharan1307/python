inputarray=[2,4,23,25,67,89,90]
n= len(inputarray)
data=int(input("Enter the number that you want to find:"))
def BinarySearch(array,n):
    first=0
    last=n-1
    midElement=(first + last )//2
    while first<= last:
        if array[midElement] == data:
            print(data ,"Element found at position ",midElement)
            return midElement
        elif array[midElement]<data:
            first=midElement+1
            midElement=(first + last)//2
        elif array[midElement]>data:
            last=midElement-1
            midElement=(first + last)//2



    print("Element not found")
    return -1



BinarySearch(inputarray,n)



