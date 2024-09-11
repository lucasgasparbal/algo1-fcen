sumaPotencias :: Int -> Int -> Int -> Int

sumaPotencias q 1 b = sumaPotenciasInterior q 1 b

sumaPotencias q a b =  sumaPotenciasInterior q a b + sumaPotencias q (a-1) b


sumaPotenciasInterior :: Int -> Int -> Int -> Int

sumaPotenciasInterior q a 1 = q^(a+1)

sumaPotenciasInterior q a b = q^(a+b) + sumaPotenciasInterior q a (b-1)


menorDivisor :: Integer -> Integer

menorDivisor n = buscarMenorDivisor n 2

buscarMenorDivisor :: Integer -> Integer -> Integer

buscarMenorDivisor n candidatoDivisor   | n == 1 = 1
                                        | mod n candidatoDivisor == 0 = candidatoDivisor
                                        | otherwise = buscarMenorDivisor n (candidatoDivisor+1)


fib :: Integer -> Integer

fib 0 = 0
fib 1 = 1
fib n = fib (n-1) +fib(n-2)

-- e17

esFibonacci :: Integer -> Bool

esFibonacci n = esFibonacciConNumSucesion n 1

esFibonacciConNumSucesion :: Integer -> Integer -> Bool

esFibonacciConNumSucesion n numSucesion | n < fib numSucesion = False
                                        | otherwise =  (n == fib numSucesion) || esFibonacciConNumSucesion n (numSucesion+1)



--e18

mayorDigitoPar :: Integer -> Integer

mayorDigitoPar n = mayorDigitoParComparando n (-1)

mayorDigitoParComparando :: Integer -> Integer -> Integer

mayorDigitoParComparando n comparativo | n < 10 && esPar n = numeroMayor n comparativo
                                       | n < 10 = comparativo
                                       | esPar (mod n 10) =  mayorDigitoParComparando (div n 10) (numeroMayor (mod n 10) comparativo)
                                       | otherwise = mayorDigitoParComparando (div n 10) comparativo


esPar :: Integer -> Bool

esPar n = mod n 2 == 0


numeroMayor :: Integer -> Integer -> Integer

numeroMayor a b | a < b = b
                | otherwise = a

--e19

esSumaInicialDePrimos :: Integer -> Bool

esSumaInicialDePrimos n = esSumaDePrimosEmpezandoPorN n 1


esSumaDePrimosEmpezandoPorN :: Integer -> Integer -> Bool

esSumaDePrimosEmpezandoPorN n numSucesion | n <  sumaDeNPrimerosPrimos numSucesion = False
                                   | otherwise = ( n == sumaDeNPrimerosPrimos numSucesion) || esSumaDePrimosEmpezandoPorN n (numSucesion + 1)


sumaDeNPrimerosPrimos :: Integer -> Integer

sumaDeNPrimerosPrimos 1 = 2

sumaDeNPrimerosPrimos n = nEsimoPrimo n + sumaDeNPrimerosPrimos (n-1)





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



--e20

tomaValorMax :: Integer -> Integer -> Integer

tomaValorMax n1 n2 = buscarValorMaximoSumaDiv n1 n2 n1


buscarValorMaximoSumaDiv :: Integer -> Integer -> Integer -> Integer

buscarValorMaximoSumaDiv n1 n2 m | n1 == n2+1 = m
                                 | sumaDivisores n1 > sumaDivisores m = buscarValorMaximoSumaDiv (n1+1) n2 n1
                                 | otherwise = buscarValorMaximoSumaDiv (n1+1) n2 m


sumaDivisores :: Integer -> Integer

sumaDivisores n = sumaDivisoresDesde n n

sumaDivisoresDesde :: Integer -> Integer -> Integer

sumaDivisoresDesde _ 1 = 1

sumaDivisoresDesde n desde | mod n desde == 0 = desde + sumaDivisoresDesde n (desde-1)
                           | otherwise = sumaDivisoresDesde n (desde-1)


--e21

pitagoras :: Integer -> Integer -> Integer -> Integer

pitagoras m n r = cantidadParesPitagoricosSobreP m n r 0


cantidadParesPitagoricosSobreP :: Integer -> Integer -> Integer -> Integer -> Integer

cantidadParesPitagoricosSobreP p q r cantidad | p == -1 = cantidad
                                              | otherwise = cantidadParesPitagoricosSobreP (p-1) q r (cantidad+ cantidadParesPitagoricosSobreQ p q r 0) 

cantidadParesPitagoricosSobreQ :: Integer -> Integer -> Integer -> Integer -> Integer

cantidadParesPitagoricosSobreQ p q r cantidad | q == -1 = cantidad
                                              | cumplenDesigualdadTriangular p q r = cantidadParesPitagoricosSobreQ p (q-1) r (cantidad+1)
                                              | otherwise = cantidadParesPitagoricosSobreQ p (q-1) r cantidad


cumplenDesigualdadTriangular :: Integer -> Integer -> Integer -> Bool

cumplenDesigualdadTriangular p q r = ((p^2) + (q^2)) <= (r^2)