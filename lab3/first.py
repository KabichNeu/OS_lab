
def firstFit(blockSize, m, processSize, n):
	
	allocation = [-1] * n

	for i in range(n):
		for j in range(m):
			if blockSize[j] >= processSize[i]:
				
				# allocate block j to p[i] process
				allocation[i] = j

				# Reduce available memory in this block.
				blockSize[j] -= processSize[i]

				break

	print(" Process No. Process Size	 Block no.")
	for i in range(n):
		print(" ", i + 1, "		 ", processSize[i],
						"		 ", end = " ")
		if allocation[i] != -1:
			print(allocation[i] + 1)
		else:
			print("Not Allocated")

if __name__ == '__main__':
	blockSize = [200, 300, 100, 300, 600]
	processSize = [313, 417, 120, 420]
	m = len(blockSize)
	n = len(processSize)

	firstFit(blockSize, m, processSize, n)
	