#include "Books.hpp"
#include "Books.cpp"
#include <string>
#include <iostream>

int main() {

    myBooks book1("Kafka on the Shore", "Haruki Miyazaki", 2002);
    myBooks book2("Dance Dance Dance", "Haruki Miyazaki", 1994);
    
    std::cout << book1.getTitle() << "\n";
    std::cout << book1.getAuthor() << "\n";
    std::cout << book1.getYear() << "\n";    
    
    std::cout << std::endl;

    std::cout << book2.getTitle() << "\n";
    std::cout << book2.getAuthor() << "\n";
    std::cout << book2.getYear() << "\n";    
    return 0;
}