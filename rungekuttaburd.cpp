#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<cmath>
#include<iomanip>


using namespace std;

int main()

{
	int i, N;
	float a, b, alpha, ftw, h, t,K1,K2, K3,K4, omega;
	float ftw1, ftw2, ftw3;
a = 0;
b = 2.0;
N = 10;
alpha = 0.5;
     

h = (b-a)/N;
t = a;
omega = alpha;

for (i = 1; i<=N; i++)
{
	ftw = omega - pow(t,2) +1;
	
    K1 = h*ftw;
    ftw1 = omega +K1/2 - pow(t+h/2,2) +1;
    K2 = h*ftw1;
    ftw2 = omega +K2/2 - pow(t+h/2,2) +1;
    K3 = h*ftw2;
    ftw3 = omega +K3 - pow(t+h,2) +1;
    K4 = h*ftw3;
    
    omega = omega +(K1 + 2*K2 + 2*K3 + K4)/6;
    t = a +i*h;
    
}
cout << omega;

	
	
	
	
	
}
