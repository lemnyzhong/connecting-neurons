#include <iostream>
#include <limits>

using namespace std;

/*
allows for mistypes of int selection 
    e.g user input: 2e
    this function allows the user to still have the 2nd selection
    without including the addition char, to avoid any errors
used to clear input buffer and ignore any char
used in conjunction with *INT* user inputs
*/
void clearBuffer() {
    cin.clear();
    cin.ignore(numeric_limits<streamsize>::max(), '\n');
}
