#include <stdio.h>
#include <stdlib.h>
#include <time.h>
typedef int element;
typedef struct ListNode {
   element data;
   struct ListNode* link;
}ListNode;
ListNode* insert_first(ListNode* head, int value)
{
   ListNode* p = (ListNode*)malloc(sizeof(ListNode));
   p->data = value;
   p->link = head;
   head = p;
   return head;
}
int sizeofList(ListNode* head)
{
   ListNode* p = head;
   int count = 0;
   while (p != NULL) {
      p = p->link;
      count++;
   }
   return count;
}
int minofList(ListNode* head)
{
   ListNode* p = head;
   int min = 0;
   while (p != NULL) {
      if (p->data < min)
         min = p->data;
      p = p->link;
   }
   return min;
}
int maxofList(ListNode* head)
{
   ListNode* p = head;
   int max = 0;
   while (p != NULL) {
      if (p->data > max)
         max = p->data;
      p = p->link;
   }
   return max;
}
ListNode* findanddelete(ListNode* head, ListNode *next, int item)
{
   ListNode *p=head;
   for (int i=0; i<sizeofList(head)-1;i++){
      if (next->data==item){
         next=next->link;
         free(head->link);
         head->link=next;
      }
      else{
         next=next->link;
         head=head->link;
      }
   }
   return p;
}
int main()
{
   ListNode* head = NULL;
   ListNode* next = NULL;
   int k;
   srand(time(NULL));
   int max = 0, min = 0, n;
   for (int i = 0; i < 100000; i++) {
      k = rand();
      head = insert_first(head, k);
   }
   printf("list size : %d\n", sizeofList(head));

   while(head->data==5001){
      head=head->link;
   }
   head=findanddelete(head, head->link, 5001);

   printf("list size: %d", sizeofList(head));

}