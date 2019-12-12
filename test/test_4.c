#include <stdio.h>
int main() {
int x= 0.0;
printf( "stored %d", x);
x= 1;
printf( "stored %d", x);
int y= 10*3+x-(9+4);
printf( "stored %d", y);
float i= 0.00;
printf( "stored %d", i);
short int t= 1;
printf( "stored %d", t);
float a= 0.0;
printf( "stored %d", a);
short int u= 1&0;
printf( "stored %d", u);
i= (0-1)*5+8/9;
printf( "stored %d", i);
return 0;
}