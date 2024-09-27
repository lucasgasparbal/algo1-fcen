module E1 where

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
                        | otherwise = x : quitarTodos elem xs