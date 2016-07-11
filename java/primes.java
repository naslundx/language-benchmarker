import java.util.ArrayList;

public class primes 
{
    public static void main(String[] args) 
	{
		final int n = 1000000;
		ArrayList primes = new ArrayList();
		primes.add(2);

		for(int i = 3; i < n; i++)
		{
			boolean isPrime = true;
			for(int j = 0; j < primes.size(); j++)
			{
				int P = (int)primes.get(j);
				if (P * P > i)
				{
					break;
				}
				if (i % P  == 0)
				{
					isPrime = false;
					break;
				}
			}

			if (isPrime)
			{
				primes.add(i);
			}
		}
    }
}
