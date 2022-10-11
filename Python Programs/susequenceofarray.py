def printSubsequences(arr, index, subarr):
	
	# Print the subsequence when reach
	# the leaf of recursion tree
	if index == len(arr):
		
		# Condition to avoid printing
		# empty subsequence
		if len(subarr) != 0:
			print(subarr)
	
	else:
		# Subsequence without including
		# the element at current index
		printSubsequences(arr, index + 1, subarr)
		
		# Subsequence including the element
		# at current index
		printSubsequences(arr, index + 1,
							subarr+[arr[index]])
	
	return
		
arr = [1, 2, 3]

printSubsequences(arr, 0, [])
