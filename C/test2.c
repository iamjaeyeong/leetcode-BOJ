#define CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#define MAX_STACK_SIZE 100
typedef int element;
typedef struct {
    element data[MAX_STACK_SIZE];
    int top;
}StackType;
void init_stack(StackType* s)
{
    s->top = -1;
}
int is_empty(StackType* s)
{
    return (s->top == -1);
}
int is_full(StackType* s)
{
    return (s->top == (MAX_STACK_SIZE - 1));
}
void push(StackType* s, element item)
{
    if (is_full(s)) {
        fprintf(stderr, "stack overflow");
        return;
    }
    else s->data[++(s->top)] = item;
}
int pop(StackType* s)
{
    if (is_empty(s)) {
        fprintf(stderr, "stack is empty\n");
        exit(1);
    }
    else return s->data[(s->top)--];
}
element peek(StackType* s)
{
    if (is_empty(s)) {
        fprintf(stderr, "stack is empty\n");
        exit(1);
    }
    else return s->data[s->top];
}
int main()
{
    StackType s;
    int input=0, prev=-100, temp;
    init_stack(&s);
    printf("Enter integers : ");
    scanf("%d", &input);
    while (1){
       if (input<=0){
          break;
       }
       else{
          push(&s, input%10);
          input/=10;
       }
    }
    do {
       temp=pop(&s);
       if (prev==temp){
          continue;
       }
       else{
          printf("%d", temp);
          prev=temp;
       }
    } while(s.top!=-1);
    return 0;
}