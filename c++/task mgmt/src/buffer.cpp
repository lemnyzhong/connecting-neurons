#include <iostream>
#include <limits>

using namespace std;

/*
used to clear input buffer and ignore any char
used in conjunction with int user inputs
*/
void clearBuffer() {
    cin.clear();
    cin.ignore(numeric_limits<streamsize>::max(), '\n');
}
