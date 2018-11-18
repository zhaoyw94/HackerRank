if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    gold = max(arr)

    for i in range(n):
        if gold == max(arr):
            arr.remove(max(arr))

    print(max(arr))
