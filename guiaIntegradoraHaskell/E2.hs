module E2 where

stockDeProducto :: [(String,Int)]-> String -> Int

stockDeProducto [] _ = 0
stockDeProducto ((producto,stock):xs) productoNombre | producto == productoNombre = stock
                                                     | otherwise = stockDeProducto xs productoNombre