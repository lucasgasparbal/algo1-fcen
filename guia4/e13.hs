f :: Int -> Int -> Int

f 1 m = sumatoriaPotencia 1 m
f n m = sumatoriaPotencia n m + f (n-1) m

sumatoriaPotencia :: Int -> Int -> Int

sumatoriaPotencia n 1 = n
sumatoriaPotencia n m = (n^m) + sumatoriaPotencia n (m-1)