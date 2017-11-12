#include <iostream>
using namespace std;

int main() {
	const double SHARE_PRICE = 35.0, COMMISSION = .02;
	int shares = 750;
	double totalAmount, commAmount, totalAmountNC; //NC stands for no commission

	totalAmountNC = shares * SHARE_PRICE;
	commAmount = totalAmountNC * COMMISSION;
	totalAmount = totalAmountNC + commAmount;

	cout << "The total amount WITHOUT commission is " << totalAmountNC
	<< "\nThe total amount of commission is " << commAmount
	<< "\nThe total amount WITH commission is " << totalAmount << endl;
	return 0;
}
