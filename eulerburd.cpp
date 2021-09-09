#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<cmath>
#include<iomanip>
using namespace std;


int main()

{
	

int N, i;
float a, b, alpha, omega, fty, h, t;

a = 0.0;
b = 2;
N = 10;
alpha = 0.5;
h = (b-a)/N;
t = a;
omega = alpha;
cout << setw(3) << t,omega;


for (i = 1; i< N+1; i++)
{

	fty = omega-pow(t, 2)+1.0;
    omega = omega +h*fty;
    t = a +i*h;
    cout << setw(12) << omega;
	

}
	
	
	
	
	
	
}
