import GHC.Base (neChar)
parteEntera :: Float -> Integer

parteEntera x = buscarParteEntera x 0

buscarParteEntera :: Float -> Integer -> Integer

buscarParteEntera x n   | x < fromInteger n = n-1
                        | otherwise = buscarParteEntera x (n+1)