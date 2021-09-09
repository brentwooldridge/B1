//
//		Conversion - Program to convert temperature from 
//					Celsius degrees into Fahrenheit:
//					Fahrenheit = Celsius * (212-32)/100 + 32
//
//
#include<cstdio>
#include<iostream>
#include<cstdlib>

using namespace std;

int main(int nNumberofagrs, char* pszArgs[])

{
	
	// enter the temperture in Celsius 
	int celsius;
	
	cout << "Enter the temperature in degrees Celsius: ";
	cin >> celsius;
	
	// Calculate conversion factor for Celsius 
	// to Fahrenheit
	int factor, fahrenheit;
	// "factor" gets 212-32
	factor = 212-32;
	
	// Use conversion factor to convert Celsius 
	// into Fahrenheit;
	
	fahrenheit = factor * celsius/100 +32;
	
	// Output the results (followed by a NewLine)
	cout << "Fahrenheit value is:";
	cout << fahrenheit << endl;
	
	// Wait until user is ready before terminating program 
	// to allow the user to see the program results
	
	cout << "Press Enter to Continue..."  << endl;
	cin.ignore(10, '\n');
	cin.get();
	return 0;
	

	
	
	
}
