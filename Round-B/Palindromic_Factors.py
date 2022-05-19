import math

def main():
    T = int(input())
    for i in range(1, T+1):
        A = int(input())
    
        result = calc(A)
        print("Case #{}: {}".format(i, result))


def isPalindrome(num):
    if num < 0 or (num % 10 == 0 and num != 0):
        return False
    ans = 0
    while num > ans:
        ans = ans * 10 + num % 10
        num //= 10
    return num == ans or num == (ans//10)

def findFactors(num):
    arr = []
    for i in range(1, math.floor(num**0.5)+1):
        if num % i == 0:
            if i not in arr:
                arr.append(i)
            if num / i not in arr:
                arr.append(num / i)
    
    return arr


def calc(A):
    result = 0

    arr = findFactors(A)
    for num in arr:
        if isPalindrome(num):
            result += 1

    return result


if __name__ == "__main__":
    main()
