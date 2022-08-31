'''
LeetCode - problem 1278
'''

	def palindromePartition(self, s: str, k: int) -> int:
		def calc(i,j):
			change=0
			while i<j:
				if s[i]!=s[j]:
					change+=1
				i+=1
				j-=1
			return change
		n=len(s)

		changes=[[0]*n for _ in range(n)]
		for i in range(n):
			for j in range(i+1,n):
				changes[i][j]=calc(i,j)

		dp=[[float('inf')]*n for _ in range(k)]
		for j in range(n):
			dp[0][j]=changes[0][j]
		for i in range(1,k):
			for r in range(i,n):
				for l in range(i,r+1):
					dp[i][r]=min(dp[i][r],dp[i-1][l-1]+changes[l][r])
		return dp[-1][-1]
