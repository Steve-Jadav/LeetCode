class Solution:
    def countPrimes(self, n: int) -> int:
        primes = [True for x in range(n)]
        totalPrimes = 0
        
        for i in range(2, len(primes)):
            if primes[i]:
                j = i
                while i * j < n:
                    primes[i*j] = False
                    j += 1
        
        for val in primes[2:]:
            if val:
                totalPrimes += 1
                
        return totalPrimes
