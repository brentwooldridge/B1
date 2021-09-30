//
// Template - provides a template to be used as the 
//			starting point
//
// The following include files define the majority of 
// functions that any given program will need 
#include<cstdio>
#include<cstdlib>
#include<iostream>

using namespace std;

int main(int nNumberofArgs, char* pszArgs[])

{
	
	// Your C++ code starts here
	
	// Wait until user is ready before terminating program
	// to allow the user to see theprogram results
	cout << "Press Enter to continue..." << endl;
	cin.ignore(10, '\n');
	cin.get();
	return 0;
	
	
}
