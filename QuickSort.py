# QuickSort Algorithm

def partition(arr, low, high):
	ind = low
	elem = arr[high]
	for i in range(low, high+1):
		if(arr[i] < elem):
			arr[i], arr[ind] = arr[ind], arr[i]
			ind += 1
	arr[ind], arr[high] = arr[high], arr[ind]
	return ind


def QuickSort(arr, low, high):
	if(low < high):
		pIndex = partition(arr, low, high)
		QuickSort(arr, low, pIndex-1)
		QuickSort(arr, pIndex+1, high)


if __name__ == "__main__":
	arr = [10, 80, 30, 90, 40, 50, 70, 5, 110, 45]
	print(arr)
	QuickSort(arr, 0, len(arr)-1)
	print(arr)
