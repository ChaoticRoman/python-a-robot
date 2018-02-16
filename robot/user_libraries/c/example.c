 /* File : example.c
  * Created by Glen Berseth
  * Date: Oct 25, 2015
  * From: https://www.cs.ubc.ca/~gberseth/blog/using-swig-to-wrap-c-for-python.html
  */
#include "example.h"

double My_variable = 3.0;

int fact(int n)
{
    if (n <= 1)
        return 1;
    else
        return n * fact(n-1);
}


int my_mod(int x, int y)
{
    return (x%y);
}
