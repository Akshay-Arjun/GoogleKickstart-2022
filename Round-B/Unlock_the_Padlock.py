import math


def main():
    T = int(input())
    for i in range(1, T+1):
        N, D = [int(n) for n in input().split(" ")]
        V = [int(n) for n in input().split(" ")]
    
        result = calc(N, D, V)
        print("Case #{}: {}".format(i, result))


def calc(N, D, V):     
    dp = [[[-1, -1] for i in range(N)] for j in range(N)]

    def recursive(i, j, k):
        if i >= j:
            return 0
        
        if dp[i][j][k] != -1:
            return dp[i][j][k]
        
        
        if k == 0:
            v1 = recursive(i+1, j, 0) + min(abs(V[i] - V[i+1]), D - abs(V[i] - V[i+1]))
            v2 = recursive(i+1, j, 1) + min(abs(V[i] - V[j]), D - abs(V[i] - V[j]))

            dp[i][j][k] = min(v1, v2)
        
        
        elif k == 1:
            v1 = recursive(i, j-1, 0) + min(abs(V[j] - V[i]), D - abs(V[j] - V[i]))
            v2 = recursive(i, j-1, 1) + min(abs(V[j] - V[j-1]), D - abs(V[j] - V[j-1]))

            dp[i][j][k] = min(v1, v2)

        return dp[i][j][k]
    
    r1 = recursive(0, N-1, 0) + min(V[0], D - V[0])
    r2 = recursive(0, N-1, 1) + min(V[N-1], D - V[N-1])
    
    return min(r1, r2)


if __name__ == "__main__":
    main()
