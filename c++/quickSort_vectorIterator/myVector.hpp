#ifndef MY_VECTOR_HPP
#define MY_VECTOR_HPP

#include <initializer_list>

template <typename T>
class MyVector {
private:
  T* arrayPointer_ = nullptr;
  int size_ = 0;
  int capacity_ = 0;

public:
  MyVector();

  MyVector(int n);
  
  MyVector(std::initializer_list<T>);

  ~MyVector();

  int size() const;

  int capacity() const;

  T& operator[](int);

  const T& operator[](int) const;

  int* begin() const;

  int* end() const;

  void swap(T* x, T* y);

  int* partition(int* low, int* high);

  void quickSort_recursive(int* low, int* high);

  void quickSort(int* low, int* high);
  
};
#endif      // MY_VECTOR_HPP