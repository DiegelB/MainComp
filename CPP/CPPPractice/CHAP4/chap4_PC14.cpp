/*This is a bank charges program
written by Ben Diegel
self-coding challenge */

#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    const double CHECKS_20 = .10,
                 CHECKS_39 = .08,
                 CHECKS_59 = .06,
                 CHECKS_60 = .04,
                 BELOW_400_FEE = 15;
    
    double beginningBalance,
        numberOfChecks,
        totalServiceFees = 0;

    cout << "Please enter the beginning balance of you account\n>>";
    cin >> beginningBalance;

    cout << "\nNow please enter the number of checks written.\n>>";
    cin >> numberOfChecks;

    if (beginningBalance < 0) {
        cout << "---WARNING YOUR ACCOUNT IS OVERDRAWN---\n";
        totalServiceFees += BELOW_400_FEE;

        if (numberOfChecks < 20) {
            totalServiceFees += (CHECKS_20 * numberOfChecks); 
        }
        else if (numberOfChecks <= 39) {
            totalServiceFees += (CHECKS_39 * numberOfChecks); 
        }
        else if (numberOfChecks <= 59) {
            totalServiceFees += (CHECKS_59 * numberOfChecks); 
        }
        else if (numberOfChecks >= 60) {
            totalServiceFees += (CHECKS_60 * numberOfChecks); 
        }
        cout << "The total ammount of bank service fees is: $" 
             << setprecision(2) << fixed << totalServiceFees << endl;
    }
    else if (beginningBalance < 400) {
        totalServiceFees += BELOW_400_FEE;
        
        if (numberOfChecks < 20) {
            totalServiceFees += (CHECKS_20 * numberOfChecks); 
        }
        else if (numberOfChecks <= 39) {
            totalServiceFees += (CHECKS_39 * numberOfChecks); 
        }
        else if (numberOfChecks <= 59) {
            totalServiceFees += (CHECKS_59 * numberOfChecks); 
        }
        else if (numberOfChecks >= 60) {
            totalServiceFees += (CHECKS_60 * numberOfChecks); 
        }
        cout << "The total ammount of bank service fees is: $" 
             << setprecision(2) << fixed << totalServiceFees << endl;
    }
    else {
        if (numberOfChecks < 20) {
            totalServiceFees = (CHECKS_20 * numberOfChecks); 
        }
        else if (numberOfChecks <= 39) {
            totalServiceFees = (CHECKS_39 * numberOfChecks); 
        }
        else if (numberOfChecks <= 59) {
            totalServiceFees = (CHECKS_59 * numberOfChecks); 
        }
        else if (numberOfChecks >= 60) {
            totalServiceFees = (CHECKS_60 * numberOfChecks); 
        }
        cout << "The total ammount of bank service fees is: $" 
             << setprecision(2) << fixed << totalServiceFees << endl;
    }
}