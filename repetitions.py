def solve(n): 
	ans = 0
	c = 0
	l = 'A'
	for i in n:
		if i == l:
			c+=1
			ans = max(c, ans)
		else: 
			l=i
			c=1
	return ans

def main():
	k = input()
	print(solve(k))

if __name__ == "__main__":
	main()