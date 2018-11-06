# MergeSort Algorithm

def Merge(arr, low, mid, high):
	left = arr[low:mid+1]
	right = arr[mid+1:high+1]
	lSize = 0
	rSize = 0
	ind = low
	while(lSize < len(left) and rSize < len(right)):
		if(left[lSize] <= right[rSize]):
			arr[ind] = left[lSize]
			ind += 1
			lSize += 1
		else:
			arr[ind] = right[rSize]
			ind += 1
			rSize += 1
	while(lSize < len(left)):
		arr[ind] = left[lSize]
		ind += 1
		lSize += 1
	while(rSize < len(right)):
		arr[ind] = right[rSize]
		ind += 1
		rSize += 1

def MergeSort(arr, low, high):
	if(low < high):
		mid = (low + high)//2
		MergeSort(arr, low, mid)
		MergeSort(arr, mid+1, high)
		Merge(arr, low, mid, high)


if __name__ == "__main__":
	arr = [575, 10, 80, 30, 90, 40, 1, 50, 70, 5, 110, 45]
	print(arr)
	MergeSort(arr, 0, len(arr)-1)
	print(arr)
