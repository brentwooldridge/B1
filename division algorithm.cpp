#include<iostream>
#include<cstdlib>
#include<cstdio>

using namespace std;

int main()

{
	int m, n, r;
	
	m = 8;
	n = 4;
	
	r = m%n;
	while (r>0){
	
		if (r == 0){
			cout << r << endl;
		}	
	
		else
		{
			n = m;
			r = n;
		}
}

}
