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

    myDeque<char> deque {'a', 'b', 'c', 'd', 'e'};

    deque.pop_front();
    // EXPECT_EQ(deque.front(), 'b');
    std::cout << deque.front() << '\n';

    deque.pop_front();
    // EXPECT_EQ(deque.front(), 'c');
    std::cout << deque.front() << '\n';

    deque.pop_front();
    // EXPECT_EQ(deque.front(), 'd');
    std::cout << deque.front() << '\n';

    deque.pop_front();
    // EXPECT_EQ(deque.front(), 'e');
    std::cout << deque.front() << '\n';
    
    deque.pop_front();
    // EXPECT_TRUE(deque.empty());
    std::cout << deque.front() << '\n';
    
    return 0;
}