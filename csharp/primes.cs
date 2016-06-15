using System.Collections;

class Primes
{
	static void Main(string[] args)
	{
		int n = 10000;
		ArrayList primes = new ArrayList();
		primes.Add(2);
		for(int i = 3; i <= n; i++)
		{
			bool isPrime = true;
			foreach(int divisor in primes)
			{
				if (i % divisor == 0)
				{
					isPrime = false;
					break;
				}
			}
			if (isPrime)
				primes.Add(i);
		}

		//foreach(int p in primes)
		//	System.Console.WriteLine(p);
	}
}
