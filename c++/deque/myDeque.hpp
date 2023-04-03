#ifndef MYDEQUE_HPP_
#define MY_DEQUE_HPP_

#include <vector>
#include <initializer_list>

template <typename T>
class myDeque {
    private:
        std::vector<T> frontVector{};
        std::vector<T> backVector{};

    public:
        myDeque();

        explicit myDeque(int n);

        myDeque(std::initializer_list<T> vals);

        T& back();
        
        const T& back() const;

        T& front();

        const T& front() const;

        // more functions


        bool empty() const;

        int size() const;

        T& operator[](int);

        const T& operator[](int) const;

};
#endif