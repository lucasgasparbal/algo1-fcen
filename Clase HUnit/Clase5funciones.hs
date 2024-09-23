module Clase5funciones where

fib :: Integer -> Integer

fib 0 = 0
fib 1 = 1
fib n = fib (n-1) + fib(n-2)


pares :: [Integer] -> [Integer]

pares [] = []

pares (x:xs) | mod x 2 == 0 && not (pertenece x xs) = x:pares xs
             | otherwise = pares xs

pertenece :: (Eq t) => t -> [t] -> Bool

pertenece _ [] = False

pertenece elem (x:xs) = (elem == x) || pertenece elem xs

generarStock :: [String] -> [(String,Int)]

generarStock [] = []

generarStock (x:xs) = (inventarioDe x (x:xs)): generarStock (quitarTodos x xs)


inventarioDe :: String -> [String] -> (String, Int)

inventarioDe producto lista = (producto, contarProductoEn producto lista)

contarProductoEn :: String -> [String] -> Int

contarProductoEn producto [] = 0
contarProductoEn producto (x:xs) | producto == x = 1 + contarProductoEn producto xs
                                 | otherwise = contarProductoEn producto xs

quitarTodos :: (Eq t) => t -> [t] -> [t]

quitarTodos _ [] = []

quitarTodos elem (x:xs) | elem == x = quitarTodos x xs
                        | otherwise = x : quitarTodos x xs