primes := VectorList<Int> new(79000) . add(2)

for (i in 3 .. 1_000_000) {
	prime := true

	for (j in 0 .. primes count) {
		if (primes[j] * primes[j] > i)
			break
		if (i % primes[j] == 0) {
			prime = false
			break
		}
	}
	if (prime) {
		primes add(i)
		i toString() println()
	}
}

