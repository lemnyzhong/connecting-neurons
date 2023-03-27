#include <iostream>
#include "myVector.hpp"
#include "myVector.cpp"

int main() {
    MyVector<int> vec {4, 56, 100, 3, 2, 67, 1};

    for(int i = 0; i < vec.size(); i++) {
        std::cout << vec[i] << " ";
    }
    std::cout << "\n";

    vec.quickSort(vec.begin(), vec.end());

    for(int i = 0; i < vec.size(); i++) {
        std::cout << vec[i] << " ";
    }
    std::cout << "\n";
    
}
