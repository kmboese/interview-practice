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

#define UPPER_BOUND 10000 //largest number random generator will generate
#define ARRAY_SIZE 6
#define ELEMENTS 4

using namespace std;

const string divider = "_____________________________________________\n";


/* Algorithms */
int fourElementSum(int *input, int n);

/* Test Functions */
void testSingle();
void testMultiple();

int main(int argc, char **argv) {
	unsigned seed = chrono::system_clock::now().time_since_epoch().count();
	mt19937 gen(seed);
	uniform_int_distribution<int>  dist(0, UPPER_BOUND);
	dist(gen);

	testSingle();
	testMultiple();
	
	return 0;
}


void testSingle() {
	cout << "Testing 4-El-Sum with one solution...\n" << divider;
	int input[ARRAY_SIZE] {1, 5, 1, 0, 6, 0};
	int n = 6;
	int solutions = fourElementSum(input, n);
	cout << "Found " << solutions << " solution\n";
	assert(solutions == 1);
}

void testMultiple() {
	cout << "\nTesting 4-El-Sum with multiple solutions...\n" << divider;
	int input[6] {1, 0, 5, 2, 0, 3};
	int n = 6; //(1 + 0 + 5 + 0) && (1 + 0 + 2 + 3)
	int solutions = fourElementSum(input, n);
	cout << "Found " << solutions << " solutions\n";
	assert(solutions == 2);
}

int fourElementSum(int *input, int n) {
	int solutions = 0;
	int count = ELEMENTS - 2;
	int sum = 0;

	for (int start = 0; start <= (ARRAY_SIZE-ELEMENTS); start++) {
		for (int middle = start+1; middle < (ARRAY_SIZE - 2); middle++) {
			sum = input[start] + input[middle];
			for (int end = middle+1; end < ARRAY_SIZE; end++) {
				if (count < ELEMENTS) {
					sum += input[end];
					count++;
				}
				//successfully found a proper sum after ELEMENTS summations
				else if (count == ELEMENTS && sum == n) {
					solutions++;
					count = ELEMENTS - 2;
					sum = input[start] + input[middle];
					continue;
				}
				//no such sum found after ELEMENTS summations
				else {
					//cout << "DEBUG: sum after unsuccessful run is " << sum << "\n";
					count = ELEMENTS - 2;
					sum = input[start] + input[middle];
					continue;
				}

			}
		}
	}
	return solutions;
}