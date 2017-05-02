def steps(numberOfStairs) :
	if (numberOfStairs == 0):
		return 0

	if (numberOfStairs == 1):
		return 1
	if (numberOfStairs == 2):
		return steps(numberOfStairs-1)+1
	if (numberOfStairs==3):
		return steps(numberOfStairs-2)+steps(numberOfStairs-1)+1
	else:
		return steps(numberOfStairs-3)+steps(numberOfStairs-2)+steps(numberOfStairs-1)


print(steps(3))