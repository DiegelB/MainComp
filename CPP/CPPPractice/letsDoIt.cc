#include <iostream>
#include <string>
using namespace std;

int main(){
	double numberOne, numberTwo, finalNumber;

	cout << "Cool calculator\n";
	cout << "Plese enter your first number\n>>";
	cin >> numberOne;
	cout << "Please enter yout second number\n>>";
	cin >> numberTwo;

	string userInput;
	cout << "Would you like to (1)add or (2)subtract\n>>";
	cin >> userInput;

	if (userInput == "1"){
		finalNumber = numberOne + numberTwo;
		cout << numberOne << " + " << numberTwo << " = " << finalNumber;
	}
	else{
		if (userInput == "2"){
			if (numberOne > numberTwo){
				finalNumber = numberOne - numberTwo;
				cout << numberOne << " - " << numberTwo << " = " << finalNumber;
			}
			else{
				finalNumber = numberTwo - numberOne;
				cout << numberTwo << " - " << numberOne << " = " << finalNumber;
			}
		}
	}
	
	string userInput2;
	cout << "\nWould you like to use it again? (1)yes (2)no\n>>";
	cin >> userInput2;
	
	if (userInput2 == "1"){
		main();
	}
	else{
		return 0;
	}

}
