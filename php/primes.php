<?php

function isPrime($num, $primes) {
    foreach($primes as $i) {
        if($num % $i == 0)
            return false;
    }

    return true;
}

$primes = array(2, 3);

for($i = 4; $i <= 100000; $i = $i + 1)
    if(isPrime($i, $primes))
        array_push($primes, $i);

?>
