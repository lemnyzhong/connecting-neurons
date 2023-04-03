#include "myDeque.cpp"
#include <iostream>

int main() {
    myDeque<char> deq{'a'};

    std::cout << deq.front();
    // for(auto i = 0; i < deq.size(); i++) {
    //     std::cout << deq[i] << '\n';
    // }
    return 0;
}