#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
    int test_case;
    scanf("%d", &test_case);

    for (;test_case>0; test_case--){
        int len, start_x, start_y, target_x, target_y;
        scanf("%d", &len);
        scanf("%d %d", &start_x, &start_y);
        scanf("%d %d", &target_x, &target_y);
        int **board=malloc(sizeof(int*)*len);
        for (int i=0; i<len;i++){
            board[i]=malloc(sizeof(int)*len);
        }
        for (int i=0; i<len; i++){
            for (int j=0; j<len; j++){
                board[i][j]=0;
            }
        }

        int **pos=malloc(sizeof(int*)*2);
        pos[0]=malloc(sizeof(int)*10000);
        pos[1]=malloc(sizeof(int)*10000);
        for (int i=0; i<2; i++){
            for (int j=0; j<10000; j++){
                pos[i][j]=0;
            }
        }
        pos[0][0]=start_y;
        pos[0][1]=start_x;
        pos[0][2]=-1;
        board[pos[0][0]][pos[0][1]]=1;
        int cnt=1;
        int idx=0;
        int idx_new=0;
        while(1){
            // printf("%d\n", cnt);
            // for (int i=0; pos[0][i]!=-1; i=i+2){
            //     printf("(%d %d) ", pos[0][i], pos[0][i+1]);
            // }
            // printf("\n");
            if (pos[0][idx]==-1){
                cnt+=1; 
                pos[1][idx_new]=-1;
                pos[0]=pos[1];
                pos[1]=malloc(sizeof(int)*10000);
                idx=0;
                idx_new=0;
                pos[1][0]=0;
                pos[1][1]=0;
            }
            if (pos[0][idx]==target_y && pos[0][idx+1]==target_x){
                break;
            }
            if (pos[0][idx]>0 && pos[0][idx+1]>1 && board[pos[0][idx]-1][pos[0][idx+1]-2]==0){
                board[pos[0][idx]-1][pos[0][idx+1]-2]=cnt;
                pos[1][idx_new]=pos[0][idx]-1;
                pos[1][idx_new+1]=pos[0][idx+1]-2;
                idx_new+=2;
                pos[1][idx_new]=0;
                pos[1][idx_new+1]=0;
            }
            if (pos[0][idx]>1 && pos[0][idx+1]>0 && board[pos[0][idx]-2][pos[0][idx+1]-1]==0){
                board[pos[0][idx]-2][pos[0][idx+1]-1]=cnt;
                pos[1][idx_new]=pos[0][idx]-2;
                pos[1][idx_new+1]=pos[0][idx+1]-1;
                idx_new+=2;
                pos[1][idx_new]=0;
                pos[1][idx_new+1]=0;
            }
            if (pos[0][idx]>1 && pos[0][idx+1]<len-1 && board[pos[0][idx]-2][pos[0][idx+1]+1]==0){
                board[pos[0][idx]-2][pos[0][idx+1]+1]=cnt;
                pos[1][idx_new]=pos[0][idx]-2;
                pos[1][idx_new+1]=pos[0][idx+1]+1;
                idx_new+=2;
                pos[1][idx_new]=0;
                pos[1][idx_new+1]=0;
            }
            if (pos[0][idx]>0 && pos[0][idx+1]<len-2 && board[pos[0][idx]-1][pos[0][idx+1]+2]==0){
                board[pos[0][idx]-1][pos[0][idx+1]+2]=cnt;
                pos[1][idx_new]=pos[0][idx]-1;
                pos[1][idx_new+1]=pos[0][idx+1]+2;
                idx_new+=2;
                pos[1][idx_new]=0;
                pos[1][idx_new+1]=0;
            }
            if (pos[0][idx]<len-1 && pos[0][idx+1]>1 && board[pos[0][idx]+1][pos[0][idx+1]-2]==0){
                board[pos[0][idx]+1][pos[0][idx+1]-2]=cnt;
                pos[1][idx_new]=pos[0][idx]+1;
                pos[1][idx_new+1]=pos[0][idx+1]-2;
                idx_new+=2;
                pos[1][idx_new]=0;
                pos[1][idx_new+1]=0;
            }
            if (pos[0][idx]<len-1 && pos[0][idx+1]<len-2 && board[pos[0][idx]+1][pos[0][idx+1]+2]==0){
                board[pos[0][idx]+1][pos[0][idx+1]+2]=cnt;
                pos[1][idx_new]=pos[0][idx]+1;
                pos[1][idx_new+1]=pos[0][idx+1]+2;
                idx_new+=2;
                pos[1][idx_new]=0;
                pos[1][idx_new+1]=0;
            }
            if (pos[0][idx]<len-2 && pos[0][idx+1]>0 && board[pos[0][idx]+2][pos[0][idx+1]-1]==0){
                board[pos[0][idx]+2][pos[0][idx+1]-1]=cnt;
                pos[1][idx_new]=pos[0][idx]+2;
                pos[1][idx_new+1]=pos[0][idx+1]-1;
                idx_new+=2;
                pos[1][idx_new]=0;
                pos[1][idx_new+1]=0;
            }
            if (pos[0][idx]<len-2 && pos[0][idx+1]<len-1 && board[pos[0][idx]+2][pos[0][idx+1]+1]==0){
                board[pos[0][idx]+2][pos[0][idx+1]+1]=cnt;
                pos[1][idx_new]=pos[0][idx]+2;
                pos[1][idx_new+1]=pos[0][idx+1]+1;
                idx_new+=2;
                pos[1][idx_new]=0;
                pos[1][idx_new+1]=0;
            }
            idx+=2;
        }
        if (test_case==0){
            printf("%d", cnt-1);
        }
        else{
            printf("%d\n", cnt-1);
        }
        for (int i=0; i<len; i++){
            free(board[i]);
        }
        free(pos[0]);
        free(pos[1]);
    }




}