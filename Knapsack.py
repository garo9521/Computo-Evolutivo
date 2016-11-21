aux = map(int, raw_input().split())
n, k = aux[0], aux[1]
weight = map(int, raw_input().split())
benefit = map(int , raw_input().split())

DP = [[0 for j in xrange(k + 1)] for i in xrange(n + 1)]

for i in xrange(n):
	for j in xrange(weight[i]):
		DP[i + 1][j] = DP[i][j]
	for j in xrange(weight[i], k + 1):
		DP[i + 1][j] = max(DP[i][j], DP[i][j - weight[i]] + benefit[i])

print "The table is:"
for i in DP:
	print i
print "The answer is:", DP[n][k]
print "The elements you need to have are: "

elements = []

while n > 0:
	if DP[n][k] != DP[n - 1][k]:
		k -= weight[n - 1];
		elements.append(n)
	n -= 1

elements.reverse()
print elements