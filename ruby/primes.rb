n = 10000
primes = [2]
(3...n).each do |num|
	isPrime = true
	(2...num).each do |divisor|
		if num % divisor == 0
			isPrime = false 
			break
		end
	end
	primes << num if isPrime
end

#primes.each{|x| puts x}
