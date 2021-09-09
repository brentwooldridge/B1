#include<iostream>
#include<cstdlib>
#include<cstdio>

void simple(int n, float *a, float *b)
{
int i;
#pragma omp parallel for
n = 10;
for (i=1; i<n; i++) /* i is private by default */
{
b[i] = (a[i] + a[i-1]) / 2.0;
}
}



