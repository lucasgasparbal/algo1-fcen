module E12 where

import E10


listaDeAmigos :: [Integer] -> [(Integer,Integer)]

listaDeAmigos [] = []

listaDeAmigos (x:xs) = generarTuplasAmigasDe x xs ++ listaDeAmigos xs

generarTuplasAmigasDe :: Integer -> [Integer] -> [(Integer, Integer)]

generarTuplasAmigasDe _ [] = []

generarTuplasAmigasDe n (x:xs) | sonAmigos n x = (n,x): generarTuplasAmigasDe n xs
                               | otherwise = generarTuplasAmigasDe n xs