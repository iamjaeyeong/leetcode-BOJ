import sys
input=sys.stdin.readline

n=int(input())

def distance(pos1, pos2):
    return pow(pow(pos1[0]-pos2[0], 2)+pow(pos1[1]-pos2[1], 2), 1/2)

def main():
    dots=int(input())
    pos=[]
    for i in range(dots):
        pos.append(list(map(int, input().split())))
    dis_mat=[[distance(pos[i], pos[j]) for i in range(dots)] for j in range(dots)]
    dp=[[None, 0] for i in range(dots)]
    dp[0]=[1, distance(pos[0], pos[1])]
    dp[1]=[0, distance(pos[0], pos[1])]
    for i in range(2, dots):
        mx=0
        tmp=-1
        for j in range(dots):
            if dis_mat[i][j]-dp[j][1]>mx:
                mx=dis_mat[i][j]-dp[i][1]
                tmp=j
        if tmp==-1:
            continue
        else:
            if dp[tmp][0]==None:
                dp[tmp][0]=i
                dp[tmp][1]=mx
                dp[i][0]=tmp
                dp[i][1]=mx
            else:
                dp[dp[tmp][0]]=[None, 0]
                dp[tmp][0]=i
                dp[i][0]=tmp
                dp[tmp][1]=mx
                dp[i][1]=mx
    ans=0
    for i in dp:
        ans+=i[1]
    print(ans)

for i in range(n):
    main()
