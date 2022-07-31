def solve(n, nums):
    i = 1
    ans = 0
    while i < n:
        if nums[i] < nums[i-1]:
            ans += nums[i-1] - nums[i]
            nums[i] = nums[i]+nums[i-1]-nums[i]
            i+=1
        else:
            i+=1
    return ans
def main():
    n = int(input())
    nums = [int(i) for i in input().split()]

    print(solve(n, nums))


if __name__ == "__main__":
    main()