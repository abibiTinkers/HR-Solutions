if __name__ == '__main__':
    l2=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        l1= [name,score]
        l2.append(l1)
    min=l1[1]
    min2=l1[1]
    for i in l2:
        if i[1]<min:
            min2=min
            min=i[1]
        elif i[1]>min:
            if i[1] < min2:
                min2=i[1]
    l3=[]
    for i in l2:
        if (i[1]==min2):
            l3.append(i[0])
    l3.sort()
    for i in l3:
        print(i)
            
        
