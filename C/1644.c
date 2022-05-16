#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

int* prime(int n){
    int *arr=malloc(sizeof(int)*(n+1));
    int *ret=malloc(sizeof(int)*(n+1));
    for (int i=2; i<n+1; i++){
        arr[i]=i;
    }
    int tmp=2, idx=0;
    for (int i=2; i<n+1; i++){
        if (arr[i]==0){continue;}
        tmp=2;
        ret[idx]=arr[i];
        idx+=1;
        while(1){
            if (tmp*i>n){break;} 
            else{arr[tmp*i]=0; tmp++;}
        }
    }
    ret[idx]=-1;
    free(arr);

    return ret;
}

int main(){
    int n;
    scanf("%d", &n);
    if (n==1){
        printf("0");
        return 0;
    }
    int *ary;
    ary=prime(n);
    int p1=0, p2=0, ans=0, sum=0;


    while(1){
        if (sum>n){
            sum-=ary[p1];
            p1+=1;
        }
        else if(sum<n){
            if (ary[p2]==-1){break;}
            sum+=ary[p2];
            p2+=1;
        }
        else{
            ans+=1;
            if (ary[p2]==-1){break;}
            sum+=ary[p2];
            p2+=1;
        }
    }
    printf("%d", ans);
    return 0;
}