module E11 where

import E9


losPrimerosNPerfectos :: Integer -> [Integer]

losPrimerosNPerfectos n = losPrimerosNPerfectosDesde n 6


losPrimerosNPerfectosDesde :: Integer -> Integer -> [Integer]

losPrimerosNPerfectosDesde 0 _ = []

losPrimerosNPerfectosDesde n candidato | esPerfecto candidato = candidato :losPrimerosNPerfectosDesde (n-1) (candidato+1)
                                       | otherwise = losPrimerosNPerfectosDesde n (candidato+1)
 


esPerfecto :: Integer -> Bool

esPerfecto n = sumatoria ( divisoresPropios n) == n

-- guia 5 ejercicio 3

sumatoria :: [Integer] -> Integer

sumatoria [] = 0
sumatoria (x:xs) = x + sumatoria xs