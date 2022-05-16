#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

typedef struct m{
    int max;
    int node;
}m;

m dfs(int**ary, int*cnt, int len, int past, int start){
    m mx;
    mx.max=len;
    mx.node=start;
    for (int i=0; i<cnt[start]; i++){
        if (ary[start][i*2]==past){
            continue;
        }
        m tmp=dfs(ary, cnt, len+ary[start][i*2+1], start, ary[start][i*2]);
        if (tmp.max>mx.max){
            mx.max=tmp.max;
            mx.node=tmp.node;
        }
    }
    return mx;
}


int main(){
    int n;
    int leaf;
    scanf("%d", &n);
    int *cnt=calloc(sizeof(int), n+1);
    int *idx=calloc(sizeof(int), n+1);
    int **ary=malloc(sizeof(int*)*(n+1));
    int *tmp=malloc(sizeof(int)*3*(n-1));
    for(int i=0; i<n-1;i++){
        scanf("%d %d %d", &tmp[i*3], &tmp[i*3+1], &tmp[i*3+2]);
        cnt[tmp[i*3]]+=1;
        cnt[tmp[i*3+1]]+=1;
    }
    for (int i=1; i<n+1; i++){
        ary[i]=malloc(sizeof(int)*2*cnt[i]);
    }
    for (int i=0; i<n-1; i++){
        ary[tmp[i*3]][idx[tmp[i*3]]]=tmp[i*3+1];
        idx[tmp[i*3]]+=1;
        ary[tmp[i*3]][idx[tmp[i*3]]]=tmp[i*3+2];
        idx[tmp[i*3]]+=1;
        ary[tmp[i*3+1]][idx[tmp[i*3+1]]]=tmp[i*3];
        idx[tmp[i*3+1]]+=1;
        ary[tmp[i*3+1]][idx[tmp[i*3+1]]]=tmp[i*3+2];
        idx[tmp[i*3+1]]+=1;
    }
    for (int i=1; i<n+1; i++){
        if (cnt[i]==1){
            leaf=i;
            break;
        }
    }
    m ans=dfs(ary, cnt, 0, -1, leaf);
    m yeah=dfs(ary, cnt, 0, -1, ans.node);
    printf("%d\n", yeah.max);

}