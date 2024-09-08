import Data.Bool (Bool(True))
esDivisible :: Int -> Int -> Bool

esDivisible n m = probarDivisibilidad n m 1

probarDivisibilidad :: Int -> Int -> Int -> Bool

probarDivisibilidad x y z | x == y*z = True
                          | x < y*z = False
                          | otherwise = probarDivisibilidad x y (z+1)