#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int sum(int arr[], int len)
{
    int sum = 0;
    for (int i = 0; i < len; i++)
    {
        sum += arr[i];
    }
    return sum;
}

void sort(int *arr, int len)
{
    printf("\nSorted Array: \n");
    for (int i = 0; i < len; i++)
    {
        int key = arr[i];
        int j = i - 1;
        while (j >= 0 && arr[j] > key)
        {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
    for (int i = 0; i < len; i++)
    {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

int main()
{
    int n = 100;
    int *arry = (int *)malloc(n * sizeof(int));
    if (arry == NULL)
    {
        fprintf(stderr, "Memory allocation failed\n");
        return 1;
    }

    srand(time(NULL)); // Seed for random numbers

    for (int i = 0; i < n; i++)
    {
        arry[i] = rand() % (1000);
    }

    printf("Array: \n");
    for (int i = 0; i < n; i++)
    {
        printf("%d ", arry[i]);
    }
    printf("\n");

    sort(arry, n);
    printf("Sum of array elements: %d\n", sum(arry, n));

    free(arry); // Free allocated memory

    return 0;
}