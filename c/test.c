#include <stdio.h>

int main(void)
{
    char c;
    printf("Enter characters : ");
    while((c=getchar()) != EOF){
      putchar(c);
    }
    return 0;
}
