sumaPotencias :: Int -> Int -> Int -> Int

sumaPotencias q 1 b = sumaPotenciasInterior q 1 b

sumaPotencias q a b =  sumaPotenciasInterior q a b + sumaPotencias q (a-1) b


sumaPotenciasInterior :: Int -> Int -> Int -> Int

sumaPotenciasInterior q a 1 = q^(a+1)

sumaPotenciasInterior q a b = q^(a+b) + sumaPotenciasInterior q a (b-1)