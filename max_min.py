# log(n) time complexity

def maxFinder(arr, low, high):
	if(low == high):
		return arr[low]
	else:
		mid = (low+high)//2
		leftMax = maxFinder(arr, low, mid)
		rightMax = maxFinder(arr, mid+1, high)
		if(leftMax > rightMax):
			return leftMax
		else:
			return rightMax

def minFinder(arr, low, high):
	if(low == high):
		return arr[low]
	else:
		mid = (low+high)//2
		leftMin = minFinder(arr, low, mid)
		rightMin = minFinder(arr, mid+1, high)
		if(leftMin < rightMin):
			return leftMin
		else:
			return rightMin


if __name__ == "__main__":
	arr = [12, 17, 5, 21, 8, 34, 16, 1]
	print(arr)
	print("Min is " + str(minFinder(arr,0, 7)))
	print("Max is " + str(maxFinder(arr,0, 7)))
