#define _CRT_SECURE_NO_WARNGINGS
#include <stdio.h>
#include <stdlib.h>

void post_dfs(char **ary, int*post, int*post_idx, char start){
    if (ary[(int)start-65][1]!='.'){
        post_dfs(ary, post, post_idx, ary[(int)start-65][1]);
    }
    if (ary[(int)start-65][2]!='.'){
        post_dfs(ary, post, post_idx, ary[(int)start-65][2]);
    }
    post[post_idx[0]]=(int)start;
    post_idx[0]+=1;
}

void pre_dfs(char **ary, int*pre, int*pre_idx, char start){
    pre[pre_idx[0]]=(int)start;
    pre_idx[0]+=1;
    if (ary[(int)start-65][1]!='.'){
        pre_dfs(ary, pre, pre_idx, ary[(int)start-65][1]);
    }
    if (ary[(int)start-65][2]!='.'){
        pre_dfs(ary, pre, pre_idx, ary[(int)start-65][2]);
    }
}

void in_dfs(char **ary, int *in, int*in_idx, char start){
    if (ary[(int)start-65][1]!='.'){
        in_dfs(ary, in, in_idx, ary[(int)start-65][1]);        
    }
    in[in_idx[0]]=(int)start;
    in_idx[0]++;
    if (ary[(int)start-65][2]!='.'){
        in_dfs(ary, in, in_idx, ary[(int)start-65][2]);
    }
}

int main(){
    int n;
    scanf("%d", &n);
    char **tmp=malloc(sizeof(char *)*n);
    char **ary=malloc(sizeof(char *)*n);
    int pre_idx[1]={0};
    int post_idx[1]={0};
    int in_idx[1]={0};
    int *pre=malloc(sizeof(int)*(n));
    int *post=malloc(sizeof(int)*(n));
    int *in=malloc(sizeof(int)*(n));
    for (int i=0; i<n; i++){
        ary[i]=malloc(sizeof(char)*3);
        tmp[i]=malloc(sizeof(char)*3);
    }
    for (int i=0; i<n; i++){
        getchar();
        scanf("%c %c %c", &tmp[i][0], &tmp[i][1], &tmp[i][2]);
    }
    for (int i=0; i<n; i++){
        ary[(int)tmp[i][0]-65][0]=tmp[i][0];
        ary[(int)tmp[i][0]-65][1]=tmp[i][1];
        ary[(int)tmp[i][0]-65][2]=tmp[i][2];
    }

    pre_dfs(ary, pre, pre_idx, 'A');
    in_dfs(ary, in , in_idx, 'A');
    post_dfs(ary, post, post_idx, 'A');
// dfs
// preorder - root left right
// inorder - left root right
// postorder - left right root
// append to ary if node is leaf node.
// idx - node

    for (int i=0; i<n; i++){
        printf("%c", pre[i]);
    }

    printf("\n");
    for (int i=0; i<n; i++){
        printf("%c", in[i]);
    }
    printf("\n");
    for (int i=0; i<n; i++){
        printf("%c", post[i]);
    }

    // int **ary=malloc(sizeof(int)*n);
    // int *pre_idx={0};
    // int *post_idx={0};
    // int *in_idx={0};
    // int *pre=malloc(sizeof(int)*n);
    // int *post=malloc(sizeof(int)*n);
    // int *in=malloc(sizeof(int)*n);
    free(in);
    free(post);
    free(pre);
    for (int i=0; i<n; i++){
        free(ary[i]);
        free(tmp[i]);
    }
    free(ary);
    free(tmp);


}
