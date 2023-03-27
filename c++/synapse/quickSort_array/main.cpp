#include <iostream>

// tried templating iterator parameter, works, but forces to
// pre-init typed ptrs in main
// template <typename T>
// void swap(typename std::vector<T>::iterator x, typename std::vector<T>::iterator y) {
//     int temp = *x;
//     *x = *y;
//     *y = temp;
// }

// separate swaps for different types. 
// void swap(std::vector<double>::iterator x, std::vector<double>::iterator y) {
//     double temp = *x;
//     *x = *y;
//     *y = temp;
// }

// void swap(std::vector<std::string>::iterator x, std::vector<std::string>::iterator y) {
//     std::string temp = *x;
//     *x = *y;
//     *y = temp;
// }

// void swap(std::vector<char>::iterator x, std::vector<char>::iterator y) {
//     char temp = *x;
//     *x = *y;
//     *y = temp;
// }

// supposing vec will always be type int
void swap(int* x, int* y) {
    int temp = *x;
    *x = *y;
    *y = temp;
}

int partition(int arr[], int low, int high) {
    int pivotVal = arr[high];
    int i = low;
    for(int j = low; j < high; j++) {
        if(arr[j] <= pivotVal) {
            swap(&arr[i], &arr[j]);
            i++;
        }
    }
    swap(&arr[i], &arr[high]);
    
    return i;
}

void quickSort_recursive(int arr[], int low, int high) {
    if(low < high) {
        int pivot_pos = partition(arr, low, high);
        quickSort_recursive(arr, low, pivot_pos-1);
        quickSort_recursive(arr, pivot_pos+1, high);
    }
}

void quickSort(int arr[], int size) {
    quickSort_recursive(arr, 0, size-1);
}

void print(int arr[], int size) {
    for(int i = 0; i < size; i++) {
        std::cout << arr[i] << " ";
    }
}

int main() {
    int a[] {5, 3, 4, 1, 2, 9, 10, 12, 14, 12, 0, 32, 54, 1, 23, 10, -1, 14, 33};
    int size = sizeof(a)/sizeof(int);
    quickSort(a, size);
    print(a, size);

    std::cout << "\n";

    int ar[] {0};
    int size1 = sizeof(ar)/sizeof(int);
    quickSort(ar, size1);
    print(ar, size1);
}