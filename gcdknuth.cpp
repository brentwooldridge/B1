#include<iostream>
#include<cstdlib>
#include<cstdio>

using namespace std;

int main()

{
	int m,n,r;
	m = 6099;
	n = 2166;
	r = m%n;
	if (r == 0)
	{
    cout << n ;
    }
	else
	{
    while (r>0)
    {
        r = m%n;
        m = n;
        n = r;
       
	}
	} cout <<" "<<m;
}
	
