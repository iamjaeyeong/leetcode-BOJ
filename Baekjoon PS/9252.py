import sys
input=sys.stdin.readline

s1=input().rstrip()
s2=input().rstrip()

dp_str=[['' for i in range(len(s2)+1)] for j in range(len(s1)+1)]
dp_len=[[0 for i in range(len(s2)+1)] for j in range(len(s1)+1)]
for i in range(len(s1)):
    for j in range(len(s2)):
        if s1[i]==s2[j]:
            dp_len[i+1][j+1]=dp_len[i][j]+1
            dp_str[i+1][j+1]=dp_str[i][j]+s1[i]
        else:
            dp_len[i+1][j+1]=max(dp_len[i+1][j], dp_len[i][j+1])
            if dp_len[i+1][j]<=dp_len[i][j+1]:
                dp_str[i+1][j+1]=dp_str[i][j+1]
            else:
                dp_str[i+1][j+1]=dp_str[i+1][j]

if s1=='' or s2=='':
    print(0)
else:
    print(dp_len[-1][-1])
    if dp_len[-1][-1]!=0:
        print(dp_str[-1][-1])


