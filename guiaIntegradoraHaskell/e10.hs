module E10 where

import E9

sonAmigos :: Integer -> Integer -> Bool

sonAmigos n m = sumatoria (divisoresPropios n) == m && sumatoria (divisoresPropios m) == n


-- guia 5 ejercicio 3

sumatoria :: [Integer] -> Integer

sumatoria [] = 0
sumatoria (x:xs) = x + sumatoria xs