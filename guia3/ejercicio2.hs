import Distribution.Simple.Utils (xargs)
absoluto :: Integer -> Integer
absoluto n | n >= 0 = n
           | otherwise = -n

maximoAbsoluto :: Integer -> Integer -> Integer

maximoAbsoluto x y | absoluto x >= absoluto y = x
                   | otherwise = y

maximo3 :: Integer -> Integer -> Integer -> Integer

maximo3 x y z = maximoAbsoluto x (maximoAbsoluto y z)

algunoCero :: Float-> Float -> Bool

algunoCero x y = (x == 0) || (y == 0)

algunoCeroPM :: Float-> Float -> Bool

algunoCeroPM _ 0 = True
algunoCeroPM 0 _ = True
algunoCeroPM _ _ = False

ambosCero :: Float -> Float -> Bool

ambosCero x y = (x == 0) && (y == 0)

ambosCeroPM :: Float -> Float -> Bool

ambosCeroPM 0 0 = True
ambosCeroPM _ _ = False

mismoIntervalo :: Float -> Float -> Bool

mismoIntervalo x y = (x <= 3 && y <= 3) || (( 3 < x && x <= 7) && ( 3 < y && y <= 7)) || ( x > 7 && y > 7)

sumaDistintos :: Integer -> Integer -> Integer -> Integer

sumaDistintos x y z | x == y && y == z = x
                    | x == y || y == z = x + z
                    | x == z = y + x
                    | otherwise = x + y + z

multiploDe :: Integer -> Integer -> Bool

multiploDe _ 0 = False
multiploDe 0 _ = True
multiploDe x y = mod x y == 0

digitoUnidades :: Integer -> Integer

digitoUnidades x = mod (absoluto x) 10

digitoDecenas :: Integer -> Integer

digitoDecenas x = mod (div (x - mod x 10) 10 ) 10