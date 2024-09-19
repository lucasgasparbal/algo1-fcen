import System.Win32 (xBUTTON1)
sacarBlancosRepetidos :: [Char] -> [Char]

sacarBlancosRepetidos [] = []
sacarBlancosRepetidos [x] = [x]
sacarBlancosRepetidos (x:y:xs) | x == ' ' && y == x = sacarBlancosRepetidos (x:xs)
                               | otherwise = x : sacarBlancosRepetidos (y:xs)


contarPalabras :: [Char] -> Integer

contarPalabras [] = 0
contarPalabras [x] | x /= ' ' = 1
                   | otherwise = 0
contarPalabras (x:y:xs) | x  /= ' ' && y == ' ' = 1 + contarPalabras (sacarBlancosRepetidos xs)
                        | otherwise = contarPalabras (sacarBlancosRepetidos (y:xs))


palabras :: [Char] -> [[Char]]

palabras [] = [[]]

palabras (x:xs) | x /= ' ' =  (x : head (palabras (sacarBlancosRepetidos xs))): tail (palabras (sacarBlancosRepetidos xs))
                | otherwise = [] : palabras (sacarBlancosRepetidos xs)

palabraMasLarga :: [Char] -> [Char]

palabraMasLarga texto = buscarPalabraMasLarga (palabras texto)


buscarPalabraMasLarga :: [[Char]] -> [Char]

buscarPalabraMasLarga [x] = x

buscarPalabraMasLarga (palabra1:palabra2:palabras) | length palabra1 >= length palabra2 = buscarPalabraMasLarga (palabra1:palabras)
                                                   | otherwise = buscarPalabraMasLarga (palabra2:palabras)


aplanar :: [[Char]] -> [Char]

aplanar [] = []

aplanar (x:xs) = x ++ aplanar xs

aplanarConBlancos :: [[Char]] -> [Char]

aplanarConBlancos [] = []

aplanarConBlancos [x] = x

aplanarConBlancos (x:xs) = x ++ " " ++ aplanarConBlancos xs

aplanarConNBlancos :: [[Char]] -> Integer -> [Char]

aplanarConNBlancos [] _ = []

aplanarConNBlancos [x] _ = x

aplanarConNBlancos (x:xs) n = x ++ generarNBlancos n ++ (aplanarConNBlancos xs n)


generarNBlancos :: Integer -> [Char]

generarNBlancos 0 = ""

generarNBlancos n = ' ' : generarNBlancos (n-1)