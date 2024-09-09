import GHC.Exts.Heap (GenClosure(FloatClosure))
f1 :: Int -> Int

f1 0 = 1
f1 n = 2^n + f1 (n-1)

f2:: Int -> Float -> Float

f2 1 q = q
f2 n q = q^n + f2 (n-1) q

f3 :: Int -> Float -> Float

f3 n q = f2 (2*n) q


f4 :: Int -> Float -> Float

f4 n q = f4Aux (2*n) n q


f4Aux :: Int -> Int -> Float -> Float

f4Aux n m q | n == m = q^n 
            | otherwise = q^n + f4Aux (n-1) m q


