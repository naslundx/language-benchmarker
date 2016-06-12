#include <vector>

int main()
{
    std::vector<int> primes;
    primes.push_back(2);
    for(int i=3; i < 100000; i++)
    {
        bool prime=true;
        for(int j=0;j<primes.size() && primes[j]*primes[j] <= i;j++)
        {
            if(i % primes[j] == 0)
            {
                prime=false;
                break;
            }
        }
        if(prime) 
        {
            primes.push_back(i);
        }
    }

    return 0;
}
