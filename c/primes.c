#include <stdlib.h>

int main()
{
    int* primes = (int*)malloc(79000 * sizeof(int));
    int prime_index = 1;
    primes[0] = 2;

    for(int i=3; i < 1000000; ++i)
    {
        int prime=1;
        for(int j=0;j<prime_index && primes[j]*primes[j] <= i;++j)
        {
            if(i % primes[j] == 0)
            {
                prime=0;
                break;
            }
        }
        if(prime == 1) 
        {
            primes[prime_index++] = i;
        }
    }

    return 0;
}
