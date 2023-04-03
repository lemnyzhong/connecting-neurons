#include "myDeque.cpp"
#include <iostream>

int main() {
    myDeque<int> deq{0,1,2,3,4,5};

    for(auto i = 0; i < deq.size(); i++) {
        std::cout << deq[i] << '\n';
    }

    return 0;
}