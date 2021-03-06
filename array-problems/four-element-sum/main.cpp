/* Four Elements Sum:
 * Problem Description: Given an array of integers, find a combination of four
 * elements in the array whose sum is equal to a given value X.
 *
 * Example: A == [1, 5, 1, 0, 6, 0], n=6
 * Output: 1 (one solution: (5 + 1 + 0 + 0) == 6
	
*/
#include <iostream>
#include <random>
#include <chrono>
#include <string>
#include <assert.h>

#define UPPER_BOUND 1000 //largest number random generator will generate
#define ARRAY_SIZE 6
#define ELEMENTS 4

using namespace std;

const string divider = "_____________________________________________\n";

//Globally define random seed
unsigned seed = chrono::system_clock::now().time_since_epoch().count();
mt19937 gen(seed);
uniform_int_distribution<int>  dist(0, UPPER_BOUND);
//dist(gen);

/* Algorithms */
int fourElementSum(int *input, int n, int size);
int FESRecursive(int *input, int bound, int solutions, int key, int index, int leftBound, int rightBound, int subtotal, int level);
void printArray(int *a, int bound, int index);

/* Test Functions */
void testSingle();
void testMultiple();
void testLarge();
void testRecursive();


int main(int argc, char **argv) {
	

	testSingle();
	testMultiple();
	testLarge();
	//testRecursive();


	/*
	int size = 5;
	int a[size] {1, 2, 3, 4, 5};
	printArray(a, size-1, 0);
	*/
	

	
	return 0;
}


void testSingle() {
	cout << "Testing 4-El-Sum with one solution...\n" << divider;
	int input[ARRAY_SIZE] {0, 0, 0, 10, 10, 6};
	int n = 6;
	int solutions = fourElementSum(input, n, 6);
	cout << "Found " << solutions << " solution\n";
	assert(solutions == 1);
}

void testMultiple() {
	cout << "\nTesting 4-El-Sum with multiple solutions...\n" << divider;
	int input[6] {1, 0, 5, 2, 0, 3};
	int n = 6; 
	int solutions = fourElementSum(input, n, 6);
	cout << "Found " << solutions << " solutions\n";
	assert(solutions == 3);
}

void testLarge() {
	int size = UPPER_BOUND / 9;
	//The average value is approx. (UPPER_BOUND / 2), so 4 of those
	// added together should be a commonly found sum for four-element-sum.
	int value = (UPPER_BOUND / 2) / 4;
	cout << "\nTesting large solution:\n" << divider;
	int input[size];
	for (int i = 0; i < size; i++)
		input[i] = dist(gen);
	int solutions = fourElementSum(input, value, size);
	cout << "Found " << solutions << " solutions\n";

}

void testRecursive() {
	cout << "\nTesting 4-El-Sum with recursive function...\n" << divider;
	int size = 6;
	int input[6] {1, 0, 5, 2, 0, 3};
	int n = 8;
	int solutions = FESRecursive(input, size, 0, n, 0, 0, size-ELEMENTS, 0, 1);
	cout << "Found " << solutions << " solutions\n"; 
}

void printArray(int *a, int bound, int index) {
	//Base case
	if (index > bound){
		cout << endl;
		return;
	}
	cout << a[index] << " ";
	printArray(a, bound, ++index);
}

int fourElementSum(int *input, int n, int size) {
	int solutions = 0;
	int aSum = 0;
	int bSum = 0;
	int cSum = 0;
	int sum = 0;

	for (int a = 0; a <= (size-ELEMENTS); a++) {
		aSum = input[a];
		for (int b = a+1; b <= (size-ELEMENTS+1); b++) {
			bSum = aSum + input[b];
			for (int c = b+1; c <= (size-ELEMENTS+2); c++) {
				cSum = bSum + input[c];
				for (int d = c+1; d <= (size-ELEMENTS+3); d++) {
					sum = cSum + input[d];
					if (sum == n) {
						cout << "Solution: (" << input[a] << ", " 
						<< input[b] << ", " << input[c] << ", " 
						<< input[d] << ")\n";
						solutions++;
					}
					//DEBUG
					/*
					else {
						cout << "Failed: (" << input[a] << ", " 
						<< input[b] << ", " << input[c] << ", " 
						<< input[d] << ")\n";
					}
					*/
				}
			}
		}
	}
	return solutions;
}

int FESRecursive(int *input, int bound, int solutions, int key, int index, int leftBound, int rightBound, int subtotal, int level) {
	if (index == bound)
		return solutions;
	/*
	//Base case: at level four
	if (level == ELEMENTS) {
		if (subtotal + input[index] == key)
			solutions++;
		else if (index == (size-1))
			return;
		else
			FESRecursive(input, size, solutions, key, ++index, leftBound, rightBound, subtotal, level);
	}
	*/
	FESRecursive(input, bound, solutions, key, ++index, leftBound, rightBound, subtotal, ++level);
}