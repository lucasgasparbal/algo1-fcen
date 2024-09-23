--1

sumaAcumulada :: (Num t) => [t] -> [t]

sumaAcumulada [] = []

sumaAcumulada (x:xs) =  sumarN x (0:  sumaAcumulada xs)


sumarN :: (Num t) => t -> [t] -> [t]

sumarN _ [] = []

sumarN n (x:xs) = (n+x) : sumarN n xs


--2

descomponerEnPrimos :: [Integer] -> [[Integer]]

descomponerEnPrimos [] = []

descomponerEnPrimos (x:xs) = descomposicionEnPrimosDe x : descomponerEnPrimos xs

descomposicionEnPrimosDe :: Integer -> [Integer]


descomposicionEnPrimosDe n
    | esPrimo n = [n]
    | otherwise =  menorDivisor n :  descomposicionEnPrimosDe (div n (menorDivisor n))


--funciones guia 4 ejercicio 16

menorDivisor :: Integer -> Integer

menorDivisor n = menorDivisorAux n 2

menorDivisorAux :: Integer -> Integer -> Integer

menorDivisorAux n candidatoDivisor | candidatoDivisor == n = n
                                   | mod n candidatoDivisor == 0 = candidatoDivisor
                                   | otherwise = menorDivisorAux n (candidatoDivisor+1)


esPrimo :: Integer -> Bool

esPrimo n = menorDivisor n == n