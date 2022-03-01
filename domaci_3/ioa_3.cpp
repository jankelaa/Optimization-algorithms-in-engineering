#include <iostream>
#include <stdio.h>

static const int cost[10][10] = {
	{0,374,200,223,108,178,252,285,240,356},
	{374,0,255,166,433,199,135,95,136,17},
	{200,255,0,128,277,821,180,160,131,247},
	{223,166,128,0,430,47,52,84,40,155},
	{108,433,277,430,0,453,478,344,389,423},
	{178,199,821,47,453,0,91,110,64,181},
	{252,135,180,52,478,91,0,114,83,117},
	{285,95,160,84,344,110,114,0,47,78},
	{240,136,131,40,389,64,83,47,0,118},
	{356,17,247,155,423,181,117,78,118,0}
};

int izracunajCenu(int* cnt, int len, int* t) {
	int tek_cost = 0;

	for (int i = 0;i < len + 2;i++)
		cnt[i] = 0;

	for (int i = 0; i < 2 * (len + 1);i++)
		cnt[t[i] - 1]++;

	for (int i = 0; i < 2 * (len + 1);i += 2)
		tek_cost += cost[t[i] - 1][t[i + 1] - 1];

	for (int i = 0;i < len + 2;i++)
		if (cnt[i] >= 4)tek_cost += 100 * (cnt[i] - 3);

	return tek_cost;
}

void SequenceToSpanningTree(int* p, int len, int* t) {
	int i, j, q = 0;
	int n = len + 2;
	int* v = new int[n];

	for (i = 0;i < n;i++)
		v[i] = 0;

	for (i = 0;i < len;i++)
		v[p[i]] += 1;

	for (i = 0;i < len;i++) {
		for (j = 0;j < n;j++) {
			if (v[j] == 0) {
				v[j] = -1;
				t[q++] = j + 1;
				t[q++] = p[i] + 1;
				v[p[i]]--;
				break;
			}
		}
	}

	j = 0;
	for (i = 0;i < n;i++) {
		if (v[i] == 0 && j == 0) {
			t[q++] = i + 1;
			j++;
		}
		else if (v[i] == 0 && j == 1) {
			t[q++] = i + 1;
			break;
		}
	}

	delete[] v;
}

void variations_with_repetition(int n, int k) {
	int min_cost = INT_MAX;
	int tek_cost;
	int q;
	int* p = new int[k];
	int* t = new int[2 * (k + 1)];
	int* final = new int[2 * (k + 1)];
	int* cnt = new int[n]();

	for (int i = 0;i < k;i++)
		p[i] = 0;

	do {

		SequenceToSpanningTree(p, k, t);

		tek_cost = izracunajCenu(cnt, k, t);

		if (tek_cost < min_cost) {
			min_cost = tek_cost;
			for (int i = 0; i < 2 * (k + 1);i++) {
				final[i] = t[i];
			}
		}

		q = k - 1;
		while (q >= 0) {
			p[q]++;
			if (p[q] == n) {
				p[q] = 0;
				q--;
			}
			else
				break;
		}
	} while (q >= 0);

	delete[]p;
	delete[]t;
	delete[]cnt;
	printf("Minimalna cena je: %d \nGrane su:", min_cost);
	for (int i = 0; i < 2 * (k + 1);i++) {
		printf(" %d", final[i]);
		if ((i + 1) % 2 == 0 && i < 2 * k)
			printf("  - ");
	}
	printf("\n");
	delete[]final;
}

int main()
{
	variations_with_repetition(10, 8);
}