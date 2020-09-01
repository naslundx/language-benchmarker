using System.Collections;

class Primes
{
	static void Main(string[] args)
	{
		ArrayList primes = new ArrayList();
		primes.Add(2);
		for(int i = 3; i < 1000000; ++i)
		{
			bool isPrime = true;
			for (int j = 0; j < primes.Count; ++j)
			{
				int divisor = (int)primes[j];
				if (divisor * divisor > i)
				{
					break;
				}
				if (i % divisor == 0)
				{
					isPrime = false;
					break;
				}
			}

			if (isPrime)
			{
				primes.Add(i);
			}
		}
	}
}
