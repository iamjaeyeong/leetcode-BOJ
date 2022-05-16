#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

void dfs(int *ans, int *check, int **edges, int*tmp, int node){
    for (int i=0; i<tmp[node]; i++){
        if (check[edges[node][i]]==1){
            continue;
        }
        else{
            check[edges[node][i]]=1;
            ans[edges[node][i]]=node;
            dfs(ans, check, edges, tmp, edges[node][i]);
        }
    }
}

int main(){
    int n;
    scanf("%d", &n);
    int **edges=malloc(sizeof(int*)*(n-1));
    int *tmp=calloc(n+1, sizeof(int));
    int *idx=calloc(n+1, sizeof(int));
    int *check=calloc(n+1, sizeof(int));
    int **new_edges=malloc(sizeof(int*)*(n+1));
    for (int i=0; i<n-1; i++){
        edges[i]=malloc(sizeof(int)*2);
    }

    for (int i=0; i<n-1; i++){
        scanf("%d %d", &edges[i][0], &edges[i][1]);
        tmp[edges[i][0]]++;
        tmp[edges[i][1]]++;
    }

    for (int i=1; i<n+1; i++){
        new_edges[i]=malloc(sizeof(int)*tmp[i]);
    }

    for (int i=0; i<n-1; i++){
        new_edges[edges[i][0]][idx[edges[i][0]]]=edges[i][1];
        idx[edges[i][0]]++;
        new_edges[edges[i][1]][idx[edges[i][1]]]=edges[i][0];
        idx[edges[i][1]]++;
    }
    int *ans=malloc(sizeof(int)*(n+1));
    dfs(ans, check, new_edges, tmp, 1);
    for(int i=2; i<n+1; i++){
        printf("%d\n", ans[i]);
    }

    free(tmp);
    free(idx);
    free(check);
    free(ans);
    for(int i=0; i<n-1;i++){
        free(edges[i]);
    }
    free(edges);
    for(int i=0; i<n+1; i++){
        free(new_edges[i]);
    }
    free(new_edges);
    return 0;

}