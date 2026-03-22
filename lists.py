if __name__ == '__main__':
    N = int(input())
    mine=[]
    cmds=[]
    for j in range(N):
        cmd=input()
        cmds.append(cmd)
    for cmd in cmds:
        parts= list(cmd.split())
        if parts[0]=="insert":
            i=int(parts[1])
            e=int(parts[2])
            mine.insert(i,e)
        elif parts[0]=="print":
            print(mine)
        elif parts[0]=="remove":
            e=int(parts[1])
            mine.remove(e)
        elif parts[0]=="append":
            e=int(parts[1])
            mine.append(e)
        elif parts[0]=="sort":
            mine.sort()
        elif parts[0]=="pop":
            mine.pop()
        elif parts[0]=="reverse":
            mine.reverse()
            
