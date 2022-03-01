#include <iostream>
#include <math.h>
using namespace std;

const int ZBIR = 711;
const int PROIZVOD = 711 * pow(100,3);

void proveri(int x1, int x2, int x3, int x4) {
    if ( x1+x2+x3+x4==ZBIR && x1 * x2 * x3 * x4 == PROIZVOD)
        cout << "x1=" << (double)x1/100 << " x2=" << (double)x2/100 << " x3=" << (double)x3/100 << " x4=" << (double)x4/100 << "\n";
}

int main(){
    int x1, x2, x3, x4,c=0;
    for (x1 = 1;x1 < ZBIR;x1++) {
        for (x2 = x1;x2 < ZBIR;x2++) {
            for (x3 = x2;x3 < ZBIR;x3++) {
                for (x4 = x3;x4 < ZBIR;x4++) {  
                    c++;
                    proveri(x1, x2, x3, x4);
                }
            }
        }
    }
    cout << "Optimizaciona funkcija se poziva " << c<<" puta";
    return 0;
}