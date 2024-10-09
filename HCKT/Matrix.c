#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void transpose_matrix(int **matrix, int rows, int cols) {

    int **new_matrix = (int **)malloc(cols * sizeof(int *));
    for (int i = 0; i < cols; i++)
        new_matrix[i] = (int *)malloc(rows * sizeof(int));

    for (int i = 0; i < rows; i++)
        for (int j = 0; j < cols; j++)
            new_matrix[j][i] = matrix[i][j];

    clock_t start_time = clock();

    printf("A portion of the transposed matrix:\n");
    for (int i = 0; i < 10 && i < cols; i++) {
        for (int j = 0; j < 10 && j < rows; j++)
            printf("%d ", new_matrix[i][j]);
        printf("\n");
    }

    clock_t end_time = clock();
     
    double time_taken = ((double)(end_time - start_time)) / CLOCKS_PER_SEC;

    printf("time taken: %f seconds\n", time_taken);;

    for (int i = 0; i < rows; i++) free(matrix[i]);
    free(matrix);
    matrix = new_matrix;

}

int** create_matrix(int rows, int cols) {
    int **matrix = (int **)malloc(rows * sizeof(int *));
    for (int i = 0; i < rows; i++)
        matrix[i] = (int *)malloc(cols * sizeof(int));

    for (int i = 0; i < rows; i++)
        for (int j = 0; j < cols; j++)
            matrix[i][j] = rand(); // Fill matrix with random numbers

    return matrix;
}

void print_matrix(int **matrix, int rows, int cols) {
    printf("A portion of the matrix:\n");
    for (int i = 0; i < 10 && i < rows; i++) {
        for (int j = 0; j < 10 && j < cols; j++)
            printf("%d ", matrix[i][j]);
        printf("\n");
    }
}

int main() {
    srand(time(NULL));
    int rows = 16384, cols = 16384;

    int **matrix = create_matrix(rows, cols);

    print_matrix(matrix, rows, cols);

    transpose_matrix(matrix, rows, cols);

    return 0;
}
