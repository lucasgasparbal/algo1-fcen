sumaDigitos :: Int -> Int

sumaDigitos n | n < 10 = n
              | otherwise = (mod n 10) + sumaDigitos (div n 10) 