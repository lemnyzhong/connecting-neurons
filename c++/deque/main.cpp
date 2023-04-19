#include "myDeque.cpp"
#include <iostream>

int main() {
    // myDeque<int> deque;
    // const int N = 1'000'000;
    // for (int i = N-1; i >=0; --i) {
    //     deque.push_front(i);
    //     std::cout << i << '\n';
    // }

    // for (int i = 0; i < N; ++i) {
    //     deque.pop_back();
    //     std::cout << i << '\n';
    // }

    // // EXPECT_TRUE(deque.empty());
    // std::cout << deque.empty() << '\n';

    // deque.push_back(23);
    // // EXPECT_EQ(deque[0], 23);
    // std::cout << deque[0];

    myDeque<int> deque {};

    deque.push_back(1);

    deque.pop_back();

    for(auto i = 0; i < deque.size(); i++) {
        std::cout << deque[i] << "\n";
    }


    std::cout << deque.front();
    
    return 0;
}
