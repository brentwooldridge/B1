#include<iostream>
using namespace std;
float f(float x);

int main(int argc, char ** argv){
	float w;
	w=f(2);
	std::cout << "The value of w is: " << w <<std::endl;

}
float f(float x){
	float y;
	
	y = x*x*x-x*x + 2;
	
	return y;
}
