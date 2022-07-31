i = int(input())
while i != 1:
	print(int(i), end=" ")
	if i%2==0:
		i/=2
	else:
		i = 3*i+1
print(1, end=" ")