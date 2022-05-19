import math

def main():
    T = int(input())
    for i in range(1, T+1):
        R, A, B = [int(n) for n in input().split(" ")]
    
        result = calc(R, A, B)
        print("Case #{}: {}".format(i, result))



def calc(R, A, B):
    area = 0
    radius = R

    while radius > 0:
        area += radius * radius
        radius = radius * A
        area += radius * radius
        radius = radius // B


    return area * math.pi


if __name__ == "__main__":
    main()
