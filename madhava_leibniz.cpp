//
//  main.cpp
//  madhava_leibniz
//
//  Created by Alexander Lopatin on 06/05/19.
//  Copyright © 2019 Alexander Lopatin. All rights reserved.
//

#include <iostream>
#include <vector>
#include <chrono>

using namespace std;
using namespace std::chrono;

auto leibniz(int k, int n) {
    auto series = new std::vector<double>(n - k + 1);
    double a[2] = { 1.0, -1.0 };
    for (int i = k; i <= n;  i++)
        (*series)[i] = a[i&1] / (double) (2*i+1);
    return series;
}

auto madhava(int k, int n) {
    auto series = new std::vector<double>(n - k + 1);
    int k2 = 2 * k + 1;
    int n2 = 2 * n + 1;
    if ((k & 1) == 0) {
        int i = 0;
        for (int divisor = k2;  divisor <= n2; divisor += 4) {
            (*series)[i] = 1.0 / divisor;
            i += 2;
        }
        i = 1;
        for (int divisor = k2 + 2;  divisor <= n2; divisor += 4) {
            (*series)[i] = -1.0 / divisor;
            i += 2;
        }
    } else {
        int i = 0;
        for (int divisor = k2;  divisor <= n2; divisor += 4) {
            (*series)[i] = -1.0 / divisor;
            i += 2;
        }
        i = 1;
        for (int divisor = k2 + 2; divisor <= n2; divisor += 4) {
            (*series)[i] = 1.0 / divisor;
            i += 2;
        }
    }
    return series;
}


int main(int argc, const char * argv[]) {
    std::cout << "Hello, World!\n";
//    1 PI = 2.66667 t1 = 14 t2 = 0
//    10 PI = 3.23232 t1 = 0 t2 = 0
//    100 PI = 3.15149 t1 = 2 t2 = 2
//    1000 PI = 3.14259 t1 = 44 t2 = 58
//    10000 PI = 3.14169 t1 = 342 t2 = 339
//    100000 PI = 3.1416 t1 = 2438 t2 = 1945
//    1000000 PI = 3.14159 t1 = 21284 t2 = 18768
//    10000000 PI = 3.14159 t1 = 204886 t2 = 190974
//    100000000 PI = 3.14159 t1 = 2039067 t2 = 1872717
//    Hello, World!
//    1 PI = 2.66667 t1 = 15 t2 = 0
//    10 PI = 3.23232 t1 = 0 t2 = 0
//    100 PI = 3.15149 t1 = 2 t2 = 2
//    1000 PI = 3.14259 t1 = 43 t2 = 45
//    10000 PI = 3.14169 t1 = 288 t2 = 378
//    100000 PI = 3.1416 t1 = 2346 t2 = 2365
//    1000000 PI = 3.14159 t1 = 21234 t2 = 20259
//    10000000 PI = 3.14159 t1 = 202143 t2 = 201120
//    100000000 PI = 3.14159 t1 = 2057860 t2 = 2006662
//    Program ended with exit code: 0
//    Hello, World!
//    100000000 PI = 3.14159 t1 = 2047624 t2 = 2043341
//    200000000 PI = 3.14159 t1 = 4049185 t2 = 4053646
//    300000000 PI = 3.14159 t1 = 6148030 t2 = 6057628
//    400000000 PI = 3.14159 t1 = 8023661 t2 = 8056124
//    500000000 PI = 3.14159 t1 = 10061067 t2 = 10018952
//    600000000 PI = 3.14159 t1 = 12045184 t2 = 12010151
//    700000000 PI = 3.14159 t1 = 16921041 t2 = 15340653
//    800000000 PI = 3.14159 t1 = 21797256 t2 = 38965005
//    900000000 PI = 3.14159 t1 = 26411504 t2 = 64860412
//    1000000000 PI = 3.14159 t1 = 31072108 t2 = 84743648
//    Program ended with exit code: 0
    for (int n = 1; n <= 100000000; n *= 10) {
        auto t1 = high_resolution_clock::now();
        auto series = madhava(0, n);
        auto t2 = high_resolution_clock::now();
        double pi = 0.0;
        for (auto it = series->begin(); it != series->end(); it++) pi += *it;
        pi *= 4.0;
        auto t3 = high_resolution_clock::now();
        auto duration1 = duration_cast<microseconds>(t2 - t1).count();
        auto duration2 = duration_cast<microseconds>(t3 - t2).count();
        cout << n << " PI = " << pi << " t1 = " << duration1 << " t2 = " << duration2 << endl;
//        if (n == 10) {
//            for (auto it = series->begin(); it != series->end(); it++)
//                cout << *it << endl;
//        }
        delete series;
    }
    return 0;
}
