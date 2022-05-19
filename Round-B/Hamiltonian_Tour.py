import math

EMPTY = "*"
BUILDING = "#"
directions = ["E", "S", "W", "N"]
dir_op = [ [0, 1], [1, 0], [0, -1], [-1, 0] ]

def main():
    T = int(input())
    for i in range(1, T+1):
        R, C = [int(n) for n in input().split(" ")]
        grid = [[BUILDING for _ in range(C*2)] for _ in range(R * 2)]
        B = []
        count = 0
        for r in range(R):
            row = input()
            B.append([c for c in row])
            for c, content in enumerate(row):
                if content == EMPTY:
                    grid[2*r][2*c] = "E"
                    grid[2*r][2*c+1] = "S"
                    grid[2*r+1][2*c] = "N"
                    grid[2*r+1][2*c+1] = "W"

                    count += 1
        

        result = calc(R, C, B, grid, count)
        print("Case #{}: {}".format(i, result))



def calc(R, C, B, grid, count):
    result = "IMPOSSIBLE"

    st = []

    st.append([0, 0])
    count -= 1
    B[0][0] = BUILDING

    while st:
        i, j = st.pop()
        for index, [di, dj] in enumerate(dir_op):
            ni = i + di
            nj = j + dj
            if 0 <= ni < R and 0 <= nj < C and B[ni][nj] == EMPTY:
                B[ni][nj] = BUILDING
                count -= 1
                if directions[index] == "E":
                    r1 = 2*i
                    c1 = 2*j+1
                    r2 = 2*i+1
                    c2 = 2*j+2
                elif directions[index] == "W":
                    r1 = 2*i+1
                    c1 = 2*j
                    r2 = 2*i
                    c2 = 2*j-1
                elif directions[index] == "S":
                    r1 = 2*i+1
                    c1 = 2*j+1
                    r2 = 2*i+2
                    c2 = 2*j
                elif directions[index] == "N":
                    r1 = 2*i
                    c1 = 2*j
                    r2 = 2*i-1
                    c2 = 2*j+1
                grid[r1][c1] = directions[index]
                grid[r2][c2] = directions[(index+2)%4]
                st.append([ni, nj])
        

    if count == 0:
        result = ""
        i = 0
        j = 0

        result += grid[i][j]
        dir = grid[i][j]

        di, dj = dir_op[directions.index(dir)]

        i += di
        j += dj

        while not (i == 0 and j == 0):
            dir = grid[i][j]
            result += dir
            di, dj = dir_op[directions.index(dir)]
            i += di
            j += dj


    return result



if __name__ == "__main__":
    main()
