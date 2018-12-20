#include <stdio.h>

int main(void) {
    char c;

    printf("請輸入一個字元：");
    c = getchar();

    putchar(c);
    putchar('\n');

    return 0;
}
