def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        print('Key', key)
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

m = int(input().strip())
ar = [int(i) for i in input().strip().split()]
insertion_sort(ar)
print(" ".join(map(str,ar)))