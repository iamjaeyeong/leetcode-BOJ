#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
    int n;
    int s;
    scanf("%d %d%*c", &n, &s);
    int *ary=malloc(sizeof(int)*n);
    char tmp[600000], *st;
    gets(tmp);
    st=strtok(tmp, " ");
    int idx=0;
    while(st!=NULL){
        ary[idx]=atoi(st);
        st=strtok(NULL, " ");
        idx+=1;
    }
    int p1=0, p2=0;
    int sum=0, ans=n+1;
    while(1){
        if (sum>=s){
            if (ans>p2-p1){
                ans=p2-p1;
            }
            sum-=ary[p1];
            p1+=1;
        }
        else {
            if (p2==n){
                break;
            }
            sum+=ary[p2];
            p2+=1;
        }

    }
    if (ans==n+1){
        printf("0");
    }
    else{
        printf("%d", ans);
    }

}