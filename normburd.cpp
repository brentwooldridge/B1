#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<cmath>
using namespace std;

int main()

{

int n, i;
float sumi, norm;

i = 0;

n = 2;

float x[] = {3.0, 4,0};



sumi = 0;

while (i < n)
    {
	sumi = sumi + x[i]*x[i];
	i++;
	}
norm = pow(sumi, 0.5);
cout<< norm;

}
