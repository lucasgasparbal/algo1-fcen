todosDigitosIguales :: Int -> Bool

todosDigitosIguales n = compararConDigito n (mod n 10)

compararConDigito :: Int -> Int -> Bool

compararConDigito n m | n < 10 = n == m
                      | otherwise = (mod n 10 == m) && compararConDigito (div n 10) m