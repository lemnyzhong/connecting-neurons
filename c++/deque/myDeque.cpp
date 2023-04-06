#include "myDeque.hpp"

#include <vector>

template <typename T>
myDeque<T>::myDeque() {};

template <typename T>
myDeque<T>::myDeque(int n) {
    std::size_t midPoint = n/2;
    for(auto i = 0; i < midPoint; i++) {
        frontVector.push_back(0);
    }
    for(auto i = 0; i < midPoint+1; i++) {
        backVector.push_back(0);
    }
}

template <typename T>
myDeque<T>::myDeque(std::initializer_list<T> vals) {
    std::size_t midPoint = vals.size()/2;

    for(auto i = vals.begin()+midPoint-1; i != vals.begin()-1; i--) {
        frontVector.push_back(*i);
    }

    for(auto i = vals.begin()+midPoint; i != vals.end(); i++) {
        backVector.push_back(*i);
    }
}

template <typename T>
void myDeque<T>::push_back(T val) {
    if(backVector.size() >= backVector.capacity()) {
        backVector.reserve(backVector.capacity()*2);
    }
    backVector.push_back(val);
}

template <typename T>
void myDeque<T>::push_front(T val) {
    if(frontVector.size() >= frontVector.capacity()) {
        frontVector.reserve(frontVector.capacity()*2);
    }
    frontVector.push_back(val);
}

template <typename T>
void myDeque<T>::pop_back() {
    if(backVector.empty() == false) {
        backVector.pop_back();
    }
    else {
        if(frontVector.size() == 1) {
            frontVector.pop_back();
        }
        // frontVector.erase(frontVector.begin());
        else {
            // rebalance
            std::size_t midPoint = frontVector.size()/2;

            for(auto i = 0; i < int(midPoint); i++) {
                backVector.push_back(std::move(frontVector[midPoint-i]));
                //frontVector.erase(frontVector.begin());
            }
            frontVector.erase(frontVector.begin(), frontVector.begin()+midPoint);

            backVector.pop_back();
        }
    }
}

template <typename T>
void myDeque<T>::pop_front() {
    if(frontVector.empty() == false) {
        frontVector.pop_back();
    }
    else {
        if(backVector.size() == 1) {
            backVector.pop_back();
        }
        else {
        std::size_t midPoint = backVector.size()/2;

        for(auto i = 0; i < int(midPoint); i++) {
            frontVector.push_back(std::move(backVector[midPoint-i]));
        }

        backVector.erase(backVector.begin(), backVector.begin()+midPoint);

        frontVector.pop_back();
        }
    }
}

template <typename T>
T& myDeque<T>::back() {
    if(backVector.empty() == true) {
        return frontVector[0];
    }
    return *(backVector.end()-1);
}

template <typename T>
const T& myDeque<T>::back() const {
    if(backVector.empty() == true) {
        return frontVector[0];
    }
    return *(backVector.end()-1);
}

template <typename T>
T& myDeque<T>::front() {
    if(frontVector.empty() == true) {
        return backVector[0];
    }
    return *(frontVector.end()-1);
}

template <typename T>
const T& myDeque<T>::front() const {
    if(frontVector.empty() == true) {
        return backVector[0];
    }
    return *(frontVector.end()-1);
}

template <typename T>
bool myDeque<T>::empty() const{
    if(frontVector.empty() && backVector.empty()) {
        return true;
    }
    return false;
}

template <typename T>
int myDeque<T>::size() const{
    return frontVector.size() + backVector.size();
}

template <typename T>
T& myDeque<T>::operator[](int i) {
    if(i < frontVector.size()) {
        return frontVector[frontVector.size() - i - 1];
    }
    else {
        return backVector[i-frontVector.size()];
    }
}

template <typename T>
const T& myDeque<T>::operator[](int i) const {
    if(i < frontVector.size()) {
        return frontVector[frontVector.size() - i - 1];
    }
    else {
        return backVector[i-frontVector.size()];
    }
}
