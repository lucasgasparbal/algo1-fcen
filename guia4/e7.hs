iesimoDigito :: Int -> Int -> Int

iesimoDigito n m =  mod (div  n (10^(cantDigitos n - m))) 10

cantDigitos :: Int -> Int

cantDigitos n | -10 < n && n < 10 = 1
              | otherwise = 1 + cantDigitos (div n 10)