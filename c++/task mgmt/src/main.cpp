#include <iostream>
#include "buffer.cpp"

using namespace std;


int main() {
    cout << "Welcome to Tsk Ops. Where we take ops of tsks srsly." << endl;
    cout << "Please select an option: " << endl;
    cout << "1. Enter Task      2. Edit Task        3. View Tasks       4. Exit" << endl;

    int choice;
    while(cin >> choice) {
        
        if(choice == 1) {
            // clearBuffer();
            cout << "Please enter a task" << endl;
        }
        else if(choice == 2) {
            // clearBuffer();
            cout << "Which task would you like to edit?" << endl;
        }
        else if(choice == 3) {
            // clearBuffer();
            cout << "Here are your current tasks." << endl;
        }
        else if(choice == 4) {
            cout << "Goodbye." << endl;
            break;
        }
        else {
            cout << "You didn't enter a proper selection. Try again." << endl;
        }

        clearBuffer();

        cout << "Please select an option: " << endl;
        cout << "1. Enter Task      2. Edit Task        3. View Tasks       4. Exit" << endl;
    }

    return 0;
}
