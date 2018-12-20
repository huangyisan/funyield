#include <stdio.h>

int main (void)
{
    int c;
    c = getchar();
    while (c == EOF) {
        putchar(c);
        printf("this is the value of EOF:%d",c);
        c = getchar();
        break;
    }
    return 0;
}
