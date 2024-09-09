iesimoDigito :: Int -> Int -> Int

iesimoDigito n m    | m == 1 = mod n 10
                    | otherwise = iesimoDigito (div n 10) (m-1)

cantDigitos :: Int -> Int

cantDigitos n = cantDigitosAux n 1

cantDigitosAux :: Int -> Int -> Int

cantDigitosAux n m | n < 10 = m
                   | otherwise = cantDigitosAux (div n 10) m+1