import java.util.ArrayList;

public class primes 
{
    public static void main(String[] args) 
	{
		int n = 10000;
		ArrayList primes = new ArrayList();
		primes.add(2);
		for(int i = 3; i < n; i++)
		{
			boolean isPrime = true;
			for(int j = 0; j < primes.size(); j++)
			{
				if ( i % (int) primes.get(j) == 0)
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

		//for(int i = 0; i < primes.size(); i++)
		//	System.out.println(primes.get(i));
    }
}
