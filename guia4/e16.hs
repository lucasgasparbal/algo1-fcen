menorDivisor :: Integer -> Integer

menorDivisor n = menorDivisorAux n 2

menorDivisorAux :: Integer -> Integer -> Integer

menorDivisorAux n candidatoDivisor | candidatoDivisor == n = n
                                   | mod n candidatoDivisor == 0 = candidatoDivisor
                                   | otherwise = menorDivisorAux n (candidatoDivisor+1)


esPrimo :: Integer -> Bool

esPrimo n = menorDivisor n == n

sonCoprimos :: Integer -> Integer -> Bool

sonCoprimos n m = mod n (menorDivisor m) /= 0 && mod m (menorDivisor n) /= 0

nEsimoPrimo :: Integer -> Integer 

nEsimoPrimo n = nEsimoPrimoAux n 1 2


nEsimoPrimoAux :: Integer -> Integer -> Integer -> Integer

nEsimoPrimoAux n m candidatoPrimo | n == m && esPrimo candidatoPrimo = candidatoPrimo
                                  | esPrimo candidatoPrimo = nEsimoPrimoAux n (m+1) (candidatoPrimo+1)
                                  | otherwise= nEsimoPrimoAux n m (candidatoPrimo+1)