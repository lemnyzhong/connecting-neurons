#include <iostream>
#include <string>

int main() {
    std::string x;
    int y;
    
    std::cout << "Hello!\n";
    
    std::cin >> x;
    std::cout << x + "\n";

    std::cin >> y;
    if(typeid(y) != typeid(std::string)) {
        std::cout << "That wasn't an int.\n";
    }
    else {
        std::cout << y + "\n";
    }
}