#ifdef _WIN32
#define LIBRARY_API extern "C" __declspec(dllexport)
#elif
#define LIBRARY_API extern "C"
#endif

#include <iostream>

/** 
 * Compute the sum an array
 * @param n number of elements
 * @param array input array
 * @return sum
 */
LIBRARY_API long long csum(int n, int *array)
{
    long long res = 0;
    for (int i = 0; i < n; ++i)
    {
        res += array[i];
    }
    return res;
}

LIBRARY_API double *add(double *a, double *b)
{
    double* res = new double[3];

    for (int i = 0; i < 3; ++i)
    {
        res[i] = a[i] + b[i];
        //std::cout << a[i] << "\n";
    }

    return res;
}
