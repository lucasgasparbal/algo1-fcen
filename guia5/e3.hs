
--1
sumatoria :: [Integer] -> Integer

sumatoria [] = 0
sumatoria (x:xs) = x + sumatoria xs

--2
productoria :: [Integer] -> Integer

productoria [] = 1

productoria (x:xs) = x * productoria xs


--3
maximo :: [Integer] -> Integer

maximo [x] = x

maximo (x:xs) | x > maximo xs = x
                 | otherwise = maximo xs


--4
sumarN :: Integer -> [Integer] -> [Integer]

sumarN n [x] = [x+n]

sumarN n (x:xs) = (n+x) : sumarN n xs

--5
sumarElPrimero :: [Integer] -> [Integer]

sumarElPrimero (x:xs) = sumarN x (x:xs)

--6
sumarElUltimo :: [Integer] -> [Integer]

sumarElUltimo lista = sumarN (ultimo lista) lista


ultimo :: [t] -> t

ultimo lista | longitud lista == 1 = head lista
             | otherwise = ultimo (tail lista)

longitud :: [t] -> Integer

longitud [] = 0
longitud lista = 1 + longitud (tail lista)

--7

pares :: [Integer] -> [Integer]

pares [] = []
pares (x:xs) | mod x 2 == 0 = x : pares xs
             | otherwise = pares xs

--8

multiplosDeN :: Integer -> [Integer] -> [Integer]

multiplosDeN _ [] = []
multiplosDeN n (x:xs) | mod x n == 0 = x : multiplosDeN n xs
                      | otherwise = multiplosDeN n xs

--9
ordenar :: [Integer] -> [Integer]

ordenar [] = []

ordenar xs = (ordenar (quitar (maximo xs) xs)) ++ [maximo xs]

quitar :: (Eq t) => t -> [t] -> [t]

quitar x xs | xs == [] = xs
            | x == head xs = tail xs
            | otherwise = (head xs) : (quitar x (tail xs))