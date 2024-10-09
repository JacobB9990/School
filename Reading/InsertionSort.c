#include <stdio.h>
#include <stdlib.h>  

int sum(int arr[], int len) { // Adds up all elements
    int sum = 0;

    for (int i = 0; i < len; i++) {
        sum = sum + arr[i];
    }

    return sum;
}


int sort(int *arr, int len) {
    printf("\nSorted Array: \n");

    for (int i = 0; i < len; i++) {
        int key = arr[i];
        int j = i - 1;

        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }

        arr[j + 1] = key;
    }

    for (int i = 0; i < len; i++) {
        printf("%d ", arr[i]);
    }

    printf("\n");

    return 0;
}

int main() {
    int arr[] = {
        56, 23, 78, 12, 90, 34, 67, 1, 45, 89, 22, 13, 5, 47, 29,
        8, 64, 3, 95, 41, 76, 58, 2, 88, 17, 10, 32, 6, 83, 19,
        37, 51, 4, 72, 14, 99, 53, 60, 11, 66, 38, 9, 71, 31, 49,
    };
    int len_arry = sizeof(arr) / sizeof(arr[0]);
    
    printf("Array: \n");

    for (int i = 0; i < len_arry; i++) {
        printf("%d ", arr[i]);
    }

    sort(arr, len_arry);

    printf("Sum of array elements: %d\n", sum(arr, len_arry));

    return 0;
}