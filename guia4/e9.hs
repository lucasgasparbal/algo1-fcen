esCapicua :: Int -> Bool

esCapicua n | n < 10 = True
            | otherwise = ((primerDigito n) == (ultimoDigito n)) && esCapicua ( numeroSinPrimeroYUltimo n )


numeroSinPrimeroYUltimo :: Int -> Int

numeroSinPrimeroYUltimo n | n < 100 = 0
                          | otherwise = div(mod n (10^((cantDigitos n)-1))) 10


primerDigito :: Int-> Int

primerDigito n = div n (10^((cantDigitos n)-1))

ultimoDigito :: Int-> Int

ultimoDigito n = mod n 10

cantDigitos :: Int -> Int

cantDigitos n = cantDigitosAux n 1

cantDigitosAux :: Int -> Int -> Int

cantDigitosAux n m | n < 10 = m
                   | otherwise = cantDigitosAux (div n 10) m+1