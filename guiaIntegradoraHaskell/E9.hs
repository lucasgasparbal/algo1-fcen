module E9 where

divisoresPropios :: Integer -> [Integer]

divisoresPropios 1 = []

divisoresPropios n = buscarDivisoresPropiosDesde n 1


buscarDivisoresPropiosDesde :: Integer -> Integer -> [Integer]

buscarDivisoresPropiosDesde n contador | n == contador = []
                                       | mod n contador == 0 = contador:buscarDivisoresPropiosDesde n (contador+1)
                                       | otherwise = buscarDivisoresPropiosDesde n (contador+1)