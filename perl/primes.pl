$n=10000;
my @primes = ();
for($i=3;$i<=$n;$i++) 
{ 
    $is_prime = 1;
    for($j=2;$j<=sqrt($i);$j++){
        if($i % $j == 0){
            $is_prime = 0;
            break;
        }
    }
    if($is_prime == 1) {
	    push @primes, $i;
    }
}
