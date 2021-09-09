#include<iostream>
using namespace std;
int main(){
	
	class SCVector{
	private:
		int dimension;  // dimension of the vector
		double *data; // pointer to array containing vector components
		
	public:
		SCVector(int dim);  //default constructor
		SCVector(const SCVector& v); // copy constructor
		SCVector(int col, const SCVector &A); //secondary constructor
		~SCVector(); //destructor
		
		int    Dimension()  const; //dimension of the vector
		double Length();  //Euclidean norm of the vector
		void   Normalize();  // normalize vector
		
		double Norm_l1();
		double Norm_l2();
		double Norm_linf();
		
		
		//**************************
		// User defined Operators
		//**************************
		int operator==(const SCVector& v) const;
		int operator!=(const SCVector& v) const;
		SCVector & operator-(const SCVector& v);
		
		double operator()(const int i) const;
		double& operator()(const int i);
		
		void Print() const;
};
	
	
	
}

