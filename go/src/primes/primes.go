package main

const N = 1000000

func main() {
    is_prime := [N]bool{}
    is_prime[2] = true

    for i := 3; i < N; i++ {
        p := true
        for j := 2; j*j <= i && p; j++ {
            if i % j == 0 {
                p = false
            }
        }
        if p {
            is_prime[i] = true
        }
    }

    primes := make([]int, 0, 79000)
    for x := 0; x < len(is_prime)-1; x++ {
        if is_prime[x] {
            primes = append(primes, x)
        }
    }
}

