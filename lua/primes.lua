local n = 100000 -- incorrect
local primes = {2}

for i = 3, n do
	local isPrime = true
	for j = 1, #primes do
		if i % primes[j] == 0 then
			isPrime = false
			break
		end
	end
	if isPrime then
		table.insert(primes, i)
	end
end
