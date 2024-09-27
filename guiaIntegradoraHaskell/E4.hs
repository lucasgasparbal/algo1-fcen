module E4 where

import E2



aplicarOferta :: [(String,Int)] -> [(String,Float)] -> [(String,Float)]

aplicarOferta _ [] = []

aplicarOferta stock ((producto,precio):precios)| stockDeProducto stock producto > 10 = (producto,precio*0.8) : (aplicarOferta stock precios)
                                               | otherwise = (producto,precio) : (aplicarOferta stock precios)