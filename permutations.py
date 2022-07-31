def solve(n):
	if n == 1:
		return 1
	if  n == 2 or n == 3: 
		return "NO SOLUTION"
		return 0
	s = ""
	if n%2==0:
		for i in range(2, n+1, 2):
			s += str(i)+' '
		for i in range(1, n, 2):
			s += str(i)+' '
	else:
		for i in range(2, n, 2):
			s += str(i)+' '
		for i in range(1, n+1, 2):
			s += str(i)+' '
	return s
def main():
	k = int(input())
	print(solve(k))

if __name__=="__main__":
	main()