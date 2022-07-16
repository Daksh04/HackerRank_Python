if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    # ans=max(arr)
    ans= float('-inf')
    arr=list(arr)
    # print(ans)
    for i in range(0,len(arr)):
        # print(i)
        if arr[i] < max(arr) and arr[i]> ans:
            ans=arr[i]
    print(ans)
