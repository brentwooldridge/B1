#include<cstdio>
#include<cstdlib>
#include<iostream>
#include"math.h"
#include"stdio.h"
using namespace std;

int main()


{
	double SUM, t;
	
	SUM = 1;
	t = 2;
	
	while (t < 200)
	{
	
		SUM = pow(0.5,t);
		t = t+2;
	
	
	}
	
	cout << SUM << endl;
	cout << t << endl;
	
	
}
