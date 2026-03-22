if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    l1=[i for i in range(x+1)]
 
    l2=[i for i in range(y+1)]
    
    l3=[i for i in range(z+1)]
    
    l4=[(x,y,z) for x in l1 for y in l2 for z in l3]
    
    l5=[list(i) for i in l4 if(i[0]+i[1]+i[2]!=n)]
    print(l5)
    
