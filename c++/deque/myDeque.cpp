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
    for(auto i = 0; i < midPoint; i++) {
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
T& myDeque<T>::back() {
    return *(backVector.end()-1);
}

template <typename T>
const T& myDeque<T>::back() const {
    return *(backVector.end()-1);
}

template <typename T>
T& myDeque<T>::front() {
    return *(frontVector.end()-1);
}

template <typename T>
const T& myDeque<T>::front() const {
    return *(frontVector.end()-1);
}

// more functions



template <typename T>
bool myDeque<T>::empty() const{
    if(frontVector.size() == 0 && backVector.size() == 0) {
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
