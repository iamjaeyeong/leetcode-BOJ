import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n = int(input())

def dfs(edges, check, history, student, ret=[]):
    if history[student]:
        ret.append(-1)
    elif check[student]:
        ret.append(student)
    else:
        check[student] = 1
        ret.append(student)
        dfs(edges, check, history, edges[student], ret=ret)

def main():
    m = int(input())
    edges = list(map(lambda x:int(x)-1, input().split()))
    
    history = [0 for i in range(m)]
    grouped = [0 for i in range(m)]
    check = [0 for i in range(m)]

    for student in range(m):
        if history[student]:
            continue
        else:
            tmp = []
            dfs(edges, check, history, student, ret=tmp)
            selected = tmp.pop()

            for i in range(len(tmp)):
                if tmp[i]==selected:
                    break
                else:
                    history[tmp[i]] = 1
            if tmp[i]==selected:
                history[tmp[i]] = 1
                grouped[tmp[i]] = 1
            else:
                history[tmp[i]] = 1
            for j in range(i+1, len(tmp)):
                history[tmp[j]] = 1
                grouped[tmp[j]] = 1

    return m - sum(grouped)

for _ in range(n):
    print(main())        
    

    
    