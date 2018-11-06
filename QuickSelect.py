# Quick Select Algorithm

def partition(arr, low, high):
	elem = arr[high]
	ind = low
	for i in range(low, high+1):
		if(arr[i] < elem):
			arr[ind], arr[i] = arr[i], arr[ind]
			ind += 1
	arr[ind], arr[high] = arr[high], arr[ind]
	return ind

def QuickSelect(arr, low, high, k):
	pIndex = partition(arr, low, high)
	if(pIndex == k):
		return arr[pIndex]
	elif(pIndex > k):
		return QuickSelect(arr, low, pIndex-1, k)
	else:
		return QuickSelect(arr, pIndex + 1, high, k)


if __name__ == "__main__":
	arr = [575, 10, 80, 30, 90, 40, 1, 50, 70, 5, 110, 45]
	for i in range(len(arr)):
		arr = [575, 10, 80, 30, 90, 40, 1, 50, 70, 5, 110, 45]
		print(QuickSelect(arr, 0, len(arr)-1, i))
