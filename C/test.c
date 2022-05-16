#include <stdio.h>
#include <stdlib.h>

int main(){
    int *str[10];
    gets(str);
    int n;
    sscanf(str, "%d", &n);
    printf("%d", n);

// sscanf - % * *은 무시, %[a-z] a~z 외 다른거 나오면 멈춤, %[^] ^뒤에 있는 거 나올 때까지 받으라는 것
// sprintf - ptr 에 저장할건데 , buffer의 형식, buffer sprintf(ptr, "%d", num);
// scanf에 1 2 3 이렇게 들어오면 1만 가져가고 공백에서 끝. 하지만 입력 buffer에는 2 3 이 남는다.
}