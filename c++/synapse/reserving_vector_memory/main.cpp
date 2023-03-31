#include <iostream>
#include <vector>

int main() {
    std::vector<int> vec(2);
    std::cout << vec.size() << '\n';
    std::cout << vec.capacity() << '\n';
    vec = {1, 2};
    vec.reserve(vec.size()*2);
    vec.push_back(4);
    std::cout << vec.size() << '\n';
    std::cout << vec.capacity() << '\n';
    std::cout << vec[1] << '\n';
    return 0;
}