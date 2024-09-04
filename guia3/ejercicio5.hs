import Distribution.Simple.Utils (xargs)

todosMenores :: (Integer,Integer,Integer)-> Bool

todosMenores (x,y,z) = (f x > g x) && (f y > g y) && (f z > g z)


f :: Integer -> Integer

f x | x <= 7 = x*x
    | otherwise = 2*x - 1

g :: Integer -> Integer

g x | even x = x `div `2
    | otherwise = 3*x+1