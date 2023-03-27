#include <vector>
#include <iostream>

void swap(int* a, int* b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int partition(std::vector<int>& vec, int low, int high) {
    int* pivot_pos = &vec[high];

    int i = low;
    for(int j = low; j < high; j++) {
        if(vec[j] <= *pivot_pos) {
            swap(&vec[i], &vec[j]);
            i++;
        }
    }
    swap(&vec[i], &vec[high]);

    return i;
}

void quickSort_recursive(std::vector<int>& vec, int low, int high) {
    if(low < high) {
        int pivot_val = partition(vec, low, high);
        quickSort_recursive(vec, low, pivot_val-1);
        quickSort_recursive(vec, pivot_val+1, high);
    }
}

void quickSort(std::vector<int>& vec, int size) {
    quickSort_recursive(vec, 0, size-1);
}

void print(std::vector<int>& vec) {
    for(auto i : vec) {
        std::cout << i << " ";
    }
}

int main() {
    std::vector<int> vec {5, 3, 4, 1, 2, 5, 5, 5, 5};
    int size = vec.size();
    quickSort(vec, size);
    print(vec);
    return 0;
}