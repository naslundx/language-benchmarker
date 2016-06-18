fn main()
{
    let mut primes = vec![2];

    for i in 3..10000 {
        let mut prime = 1;
        for j in 0..primes.len() {
            if i % primes[j] == 0 {
                prime = 0;
                break;
            }
        }
        if prime == 1 {
            primes.push(i);
        }
    }
}
