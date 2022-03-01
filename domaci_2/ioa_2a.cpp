#include <iostream>
#include <algorithm>
#include <math.h>
using namespace std;

static const int N = 8;
static const double x[] = { 62.0,57.5,51.7,67.9,57.7,54.2,46.0,34.7 };
static const double y[] = { 58.4,56.0,56.0,19.6,42.1,29.1,45.1,45.1 };

double proracun(int niz[]) {
	double ret=0;
	for (int i = 1; i < N;i++) {
		ret += sqrt( pow(x[niz[i - 1]] - x[niz[i]],2) + pow(y[niz[i - 1]] - y[niz[i]], 2));
	}
	return ret;
}

int main()
{
	int niz[N] = { 0,1,2,3,4,5,6,7 };
	int redosled[N];
	copy(niz, niz + 8, redosled);
	double min= proracun(niz);
	while (next_permutation(niz, niz + 8)){
		double razdaljina = proracun(niz);
		if (razdaljina < min) {
			min = razdaljina;
			copy(niz, niz + 8, redosled);
		}
	} 
	cout << "Najkraca duzina je " << min;
	cout << "\nRedosled obilaska je:\n";
	for (int i = 0;i < N;i++) {
		cout << redosled[i] + 1 << " ";
	}
}