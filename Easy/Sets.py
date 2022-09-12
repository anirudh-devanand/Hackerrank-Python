def average(array):
    s=0.0
    array=set(array)
    for i in array:
        s+=i
    avg=s/(len(array))
    return round(avg,3)
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)