#include<stdio.h>
int main(void)
{
  char a[100];
  scanf("%s", a);
  int count = 0;
  char tmp;
  while (a[count] != '\0')
  {
  	if (count % 2 == 0)
    {
     	tmp = a[count];
      	a[count] = a[count + 1];
      	a[count + 1] = tmp;
    }
    count++;
  }
  printf("%s", a);
}
