#include<iostream>
#include<fstream>
#include<random>
#include<string>
#include<iomanip>
#include<vector>
#include<cstdlib>
using namespace std;


class Player{
public:
    string name, hand;
    double funds, betAmount;
    int score, wins, losses;
};

const int HAND_SIZE = 7;

//prototypes
string startScreen(fstream &userNameFile, fstream &passwordFile);
void mainMenu(Player P1);
void lineDraw(int x);

int main(){
    string temp;
    Player P1Hand[HAND_SIZE], P2Hand[HAND_SIZE], CPUHand[HAND_SIZE];
    Player P1, P2, CPU;

    fstream userNameFile, passwordFile;

    userNameFile.open("usernames.txt", ios::app);
    passwordFile.open("passwords.txt", ios::app);

    P1.name = startScreen(userNameFile, passwordFile);
    mainMenu(P1);

    userNameFile.close();
    passwordFile.close();
}

string startScreen(fstream &userNameFile, fstream &passwordFile){  
    int userInput = 0;
    string userName, password, temp;
    vector<string> userNames;
    vector<string> passwords;
    fstream readFile; 

    readFile.open("usernames.txt", ios::in);
    // todo put a way to populate the vectors with the usernams and passwords from the files
    // that will be used for username authentication (and password matching a[0] username == b[0] password)
    lineDraw(49);
    cout << "\n|\t\t\t\t\t\t|\n"
            "|\t\t(1)LOGIN\t\t\t|\n"
            "|\t\t(2)NEW PROFILE\t\t\t|\n"
            "|\t\t\t\t\t\t|\n";
    lineDraw(49);
    cout << endl;
    
    // todo add better input val and user prompts
    while(userInput != 1 || userInput != 2){
        cout << ">>";
        cin >> userInput;

        if (userInput == 2){
            cout << "Please enter a username.\n>>";
            cin >> userName;

            userNameFile << userName << endl;
            
            cout << "Please enter a password " << userName << ".\n>>";
            cin >> password;

            passwordFile << password << endl;
            return userName;
        }
        else if (userInput == 1){
            cout << "Please enter your username.\n>>";
            cin >> userName;

            return userName;
        }
    }   
}

void mainMenu(Player P1){
    char userInput;
    cout << "\t\t--Welcome to Blackjack CASINO!!!--\n\n";
    cout << "Player: " << P1.name << endl;
    cout << "1. Player VS CPU\n";
    cout << "2. Multiple Players VS CPU\n";
    cout << "3. Player Stats\n";
    cout << "4. Exit\n\n>>";

    cin >> userInput;
    switch (userInput){
        case 1:
            cout << userInput << endl;
            //singleplayer(P1);
        case 2:
            cout << userInput << endl;
            //multiplayer(P1);
        case 3:
            cout << userInput << endl;
            //stats(P1);
        case 4:
            exit(0);
    }

}

void lineDraw(int x){
    int i;
    for (i =0; i < x; i++){
        cout << "-";
    }
}