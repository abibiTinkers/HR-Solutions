if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    max=max2=-100
    for i in arr:

        if i>max:
            max2=max
            max=i
        elif i<max:
            if i> max2:
                max2=i
    print(max2)
    
