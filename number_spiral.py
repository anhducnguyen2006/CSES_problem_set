def solve(y, x):
	z = 0;
	if x > y:
		if x % 2 == 1:
   	    		z = x**2-(y-1)
		else:
			z = (x-1)**2+y
	else:
		if y % 2 == 1:
			z  = (y-1)**2+x
		else:
			z = y**2-(x-1)
	return z

def main():
	k = int(input())
	for i in range(k):
		y, x = map(int, input().split())
		print(solve(y,x))

if __name__=="__main__":
	main()