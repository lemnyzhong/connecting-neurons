#include <iostream>
#include <vector>

int main() {
    std::vector<int> vec{1,2};


    vec.reserve(vec.capacity()*2);
    
    std::size_t startingSize = vec.size();

    // std::cout << vec.size() << '\n';
    // std::cout << vec.capacity() << '\n';
    // for(auto i : vec){
    //     std::cout << i << '\n';
    // }

    for(auto i = vec.begin(); i < vec.begin()+startingSize; i++) {
        vec.push_back(*i);
    }

    vec.erase(vec.begin(), vec.begin()+startingSize);

    vec.insert(vec.begin(), 12);

    std::cout << vec.size() << '\n';
    std::cout << vec.capacity() << '\n';
    for(auto i : vec){
        std::cout << i << '\n';
    }

    return 0;
}