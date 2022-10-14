

def checkJobs(startin, endin, n):

	
	a = []
	for i in range(0, n):
		a.append([startin[i], endin[i]])
		

	a.sort()



	tv1 = a[0][1]
	tv2 = a[1][1]

	for i in range(2, n):
		
		
		if (a[i][0] >= tv1) :

			tv1 = tv2
			tv2 = a[i][1]

		
		else if (a[i][0] >= tv2) :
			tv2 = a[i][1]

		else:
			return 0
	
	return 1


if __name__ == '__main__':
	startin = [1, 2, 4] # starting time of jobs
	endin = [2, 3, 5] # ending times of jobs
	n = 3
	print(checkJobs(startin, endin, n))

