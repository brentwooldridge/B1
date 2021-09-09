//BoolTest - compare variable input from the keyboard
//			 and store the rsults off into a logical variable





#include<cstdio>
#include<cstdlib>
#include<iostream>

using namespace std;

int main(int nNumberofArg, char* pszArgs[])

{
	// Set outout format for bool variables
	// to true and false instead of 1 and 0
	
//	cout.setf(cout.boolalpha);
	
	// input two values
	int nArg1;
	cout << "Input value 1: " ;
	cin >> nArg1 ;
	
	//compare the two variables and store the results
	int nArg2;
	cout << "Input value 2: ";
	cin >> nArg2;
	bool b;
	b = nArg1 == nArg2;
	
	cout << "The statement, " << nArg1
		 << " equals "		  << nArg2
		 << " is "			  << b
		 << endl;
		 
	// wait until the user is ready beore terminating program
	// to allow the user to see the program results
	
	cout << "Press Enter to continue..."  << endl;
	cin.ignore(10, '\n');
	cin.get();
	return 0;
	
	
	
	
}
