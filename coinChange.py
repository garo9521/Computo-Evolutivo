aux = map(int, raw_input().split())
n, money = aux[0], aux[1]
coins = map(int, raw_input().split())

DP = [[0 for j in xrange(money + 1)] for i in xrange(n + 1)]
DP[1] = [i for i in xrange(money + 1)]

for i in xrange(2, n + 1):
	for j in xrange(coins[i - 1]):
		DP[i][j] = DP[i - 1][j]
	
	for j in xrange(coins[i - 1], money + 1):
		DP[i][j] = min(DP[i - 1][j], DP[i][j - coins[i - 1]] + 1)

print "The table is:"

for i in DP:
	print i

print "The answer is: ", DP[n][money]

elements = []

while money > 0:
	if DP[n][money] == DP[n - 1][money]:
		n -= 1
	else:
		elements.append(coins[n - 1])
		money -= coins[n - 1]

print "the elements are:", elements 