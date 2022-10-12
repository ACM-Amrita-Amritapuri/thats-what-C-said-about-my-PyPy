
def balancedTernary(n):

	output = ""
	
	while(n > 0):
		rem = n % 3
		n = n // 3
		
		if(rem == 2):
			rem = -1
			n += 1

		if(rem == 0):
			output = '0' + output
		else:
			if(rem == 1):
				output = '1' + output
			else:
				output = 'Z' + output

	return output


n = 238


print("Equivalent Balanced Ternary of",
	n , "is:", balancedTernary(n))

