#include <iostream>
#include <initializer_list>
#include "myVector.hpp"

template <typename T>
MyVector<T>::MyVector() {}

template <typename T>
MyVector<T>::MyVector(int n) {
  size_ = capacity_ = n;
  arrayPointer_ = new int[size_];
  for(int i = 0; i < size_; i++) {
    arrayPointer_[i] = 0;
  }
}

template <typename T>
MyVector<T>::MyVector(std::initializer_list<T> other) {
  size_ = capacity_ = other.size();
  arrayPointer_ = new T[size_];
  int i = 0;
  for (auto x : other) {
    arrayPointer_[i++] = x;
  }
}

template <typename T>
MyVector<T>::~MyVector() {
  delete[] arrayPointer_;
}

template <typename T>
int MyVector<T>::size() const {
  return size_;
}

template <typename T>
int MyVector<T>::capacity() const {
  return capacity_;
}

template <typename T>
T& MyVector<T>::operator[](int i) {
  return arrayPointer_[i];
}

template <typename T>
const T& MyVector<T>::operator[](int i) const {
  return arrayPointer_[i];
}

template <typename T>
int* MyVector<T>::begin() const {
  return arrayPointer_;
}

template <typename T>
int* MyVector<T>::end() const {
  return arrayPointer_ + size_;
}

template <typename T>
void MyVector<T>::swap(T* x, T* y) {
  int temp = *x;
  *x = *y;
  *y = temp;
}

template <typename T>
int* MyVector<T>::partition(int *low, int *high) {
  int pivot = *high;

  int* i = low;
  for(auto j = low; j != high; j++) {
    if(*j <= pivot) {
      MyVector<T>::swap(i, j);
      // int temp = *i;
      // *i = *j;
      // *j = temp;
      i++;
    }
  }
  MyVector<T>::swap(i, high);
  // int temp2 = *i;
  // *i = *high;
  // *high = temp2;
  return i;
}

template <typename T>
void MyVector<T>::quickSort_recursive(int* low, int* high) {
  if(low > high) {
    return;
  }
  int* pivotPos = partition(low, high);
  quickSort_recursive(low, pivotPos-1);
  quickSort_recursive(pivotPos+1, high);
}

template <typename T>
void MyVector<T>::quickSort(int* low, int* high) {
  quickSort_recursive(low, high-1);
}
