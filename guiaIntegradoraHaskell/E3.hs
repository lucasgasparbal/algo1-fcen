module E3 where


dineroEnStock :: [(String, Int)] -> [(String,Float)] -> Float

dineroEnStock [] _ = 0

dineroEnStock ((nombre,cantidad):inventario) precios = fromIntegral cantidad*buscarPrecio nombre precios + dineroEnStock inventario precios


buscarPrecio :: String -> [(String, Float)] -> Float

buscarPrecio _ [] = 0
buscarPrecio nombre ((producto,precio):precios) | nombre == producto = precio
                                                | otherwise = buscarPrecio nombre precios