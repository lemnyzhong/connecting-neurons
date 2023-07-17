#include <iostream>
#include <string>
#include <limits>

using namespace std;

int main() {
    std::string x;
    int y;
    
    cout << "Hello!" << endl;
    
    // std::cin >> x;
    // std::cout << x + "\n";

    // if((cin >> y)) {
    //     cout << y << endl;
    // }
    // else {
    //     cout << "That wasn't an int." << endl;
    //     cin.clear();
    //     cin.ignore(numeric_limits<streamsize>::max(), '\n');
    // }

    if(!(cin >> y)) {
        cout << "That wasn't an int." << endl;
    }
    else {
        cout << y << endl;
    }
    cin.clear();
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    cin >> x;
    cout << x;

    return 0;
}