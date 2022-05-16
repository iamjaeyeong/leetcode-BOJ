#include <stdio.h>
#define MAX_DEGREE 101
typedef struct {
   int degree;
   float coef[MAX_DEGREE];
}polynomial;

polynomial poly_multi(polynomial A, polynomial B)
{
   polynomial C;
   
   int Apos = 0, Bpos = 0, Cpos = 0;
   for (int i = Apos; i <= A.degree; i++) {
      for (int j = Bpos; j <= B.degree; j++) {
         C.coef[i+j] += A.coef[i] * B.coef[j];
      }
   }
   C.degree = A.degree + B.degree;
   return C;
}
void print_poly(polynomial p)
{
   for (int i = p.degree; i > 0; i--) {
      printf("%3.1fx^%d + ", p.coef[p.degree - i], i);
   }
   printf("%3.1f\n", p.coef[p.degree]);
}
int main()
{
   polynomial a = { 5,{3, 6, 0, 0, 0, 10} };
   polynomial b = { 4,{7,0,5,0,1} };
   polynomial c;
   print_poly(a);
   print_poly(b);
   c = poly_multi(a, b);
   printf("---------------------------\n");
   print_poly(c);
   return 0;
}