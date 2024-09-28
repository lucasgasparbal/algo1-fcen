module E8 where


esCaminoFibo :: [Integer] -> Integer -> Bool

esCaminoFibo [] _ = True

esCaminoFibo (x:xs) n = x == fib n && esCaminoFibo xs (n+1)


fib :: Integer -> Integer

fib 0 = 0
fib 1 = 1

fib n = fib(n-2)+fib(n-1)